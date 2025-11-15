# -*- coding: utf-8 -*-
"""
Simplified 2-Axis Gimbal Controller (AZ/EL) — Galil-safe (NSC-G3-E)
- Absolute/relative steering (axis moves only when needed)
- Safe motion limits
- EL mapping: 0° EL_gimbal = Up; EL_sky (0°=Horizon, +90°=Up) → EL_gimbal = EL_sky - 90°
- All Galil commands are axis-qualified (X=AZ, Y=EL) to avoid '?' rejects on BG/AM/PR.
"""

import time
import numpy as np
from pathlib import Path

try:
    import gclib
except ImportError:
    gclib = None

# ------------------- USER LIMITS -------------------
AZ_MIN, AZ_MAX = -90.0, 90.0      # -90=West, +90=East (about North=0)
EL_MIN, EL_MAX = -90.0, 90.0      # -90=North horizon, 0=Up, +90=South horizon
MAX_STEP_DEG = 20.0               # Max per-command step (deg) for relative moves
# --------------------------------------------------

STATE_FILE = "dependencies/gimbal_state/currGimbalPosition.txt"

# Skip PR if BOTH axes would move by less than this many counts
MIN_PR_COUNTS = 10  # small deadband to avoid PR 0/±1 chatter

# Axis mapping (keep it explicit)
AXIS_AZ = 'X'
AXIS_EL = 'Y'

def _clip(v, lo, hi):
    return max(lo, min(hi, v))

def _safe_load_pos():
    try:
        p = Path(STATE_FILE)
        if not p.exists():
            return [0.0, 0.0, 0.0]
        vals = np.loadtxt(p)
        return [float(vals[0]), float(vals[1]), float(vals[2])]
    except Exception:
        return [0.0, 0.0, 0.0]

def _safe_save_pos(vec3):
    try:
        Path(STATE_FILE).parent.mkdir(parents=True, exist_ok=True)
        np.savetxt(STATE_FILE, np.asarray(vec3))
    except Exception as e:
        print(f"[WARN] Could not save position: {e}")

class GimbalController:
    def __init__(self, connection, cnt_per_deg=(10000, 10000), assume_zero_on_connect=True):
        """
        assume_zero_on_connect=True:
          Immediately define current counts as 0,0 on connect without moving hardware.
          (DP X=0; DP Y=0 with motors off, then SH per axis.)
        """
        print("[INIT] Connecting to Galil Controller...")
        self.cnt_az, self.cnt_el = cnt_per_deg
        self.curr_az, self.curr_el = 0.0, 0.0
        self.curr_pos = _safe_load_pos()
        self._assume_zero = assume_zero_on_connect

        self.sim = gclib is None
        if not self.sim:
            self.g = gclib.py()
            self.g.GOpen(connection)
            try:
                self.g.timeout = 20000  # ms
            except Exception:
                pass
            print(self.g.GInfo())
            self._setup_motion()
            self._sync_from_controller()
        else:
            print("[SIMULATION MODE]")

    def _cmd(self, s):
        try:
            return self.g.GCommand(s)
        except Exception:
            print(f"[GALIL ERROR] Command failed: {s}")
            raise

    def _setup_motion(self):
        """Initialize motor parameters. Zero commanded counts (no motion) with motors OFF, then enable."""
        self._cmd("AB")
        self._cmd("ST")
        self._cmd("WT 20")

        if self._assume_zero:
            self._cmd(f"MO {AXIS_AZ}; MO {AXIS_EL}")               # motors OFF per axis
            self._cmd(f"DP {AXIS_AZ}=0; DP {AXIS_EL}=0")           # commanded position = 0,0

        self._cmd(f"SH {AXIS_AZ}; SH {AXIS_EL}")                   # enable servos per axis
        self._cmd(f"AC {AXIS_AZ}=900000; AC {AXIS_EL}=900000")
        self._cmd(f"DC {AXIS_AZ}=900000; DC {AXIS_EL}=900000")
        self._cmd(f"SP {AXIS_AZ}=40000; SP {AXIS_EL}=40000")
        print("[OK] Motion parameters set. (DP 0,0 applied)" if self._assume_zero else "[OK] Motion parameters set.")

    def _sync_from_controller(self):
        """Sync software pose from controller counts."""
        try:
            # Read each axis explicitly (works on strict parsers)
            cx = float(self._cmd(f"TP {AXIS_AZ}").strip())
            cy = float(self._cmd(f"TP {AXIS_EL}").strip())
            self.curr_az = cx / self.cnt_az
            self.curr_el = cy / self.cnt_el
            self.curr_pos = [self.curr_az, self.curr_el, 0.0]
            print(f"[SYNC] AZ={self.curr_az:.3f}°, EL_gimbal={self.curr_el:.3f}°")
        except Exception as e:
            print(f"[WARN] Could not sync from TP: {e}")

    def close(self):
        if not self.sim:
            self._cmd("ST")
            self.g.GClose()
        _safe_save_pos(self.curr_pos)
        print("[CLOSED] Gimbal safely disconnected.")

    # ---------------- HELPER: queue/begin/wait per-axis ----------------
    def _queue_begin_wait(self, dcnt_x, dcnt_y, wait=True):
        """Queue PR per axis, then BG/AM only for axes that actually move."""
        cmds = []
        if abs(dcnt_x) >= MIN_PR_COUNTS:
            cmds.append(f"PR {AXIS_AZ}={dcnt_x}")
        if abs(dcnt_y) >= MIN_PR_COUNTS:
            cmds.append(f"PR {AXIS_EL}={dcnt_y}")
        if not cmds:
            return False  # nothing to do
        self._cmd("; ".join(cmds))

        # Begin only those axes
        if abs(dcnt_x) >= MIN_PR_COUNTS:
            self._cmd(f"BG {AXIS_AZ}")
        if abs(dcnt_y) >= MIN_PR_COUNTS:
            self._cmd(f"BG {AXIS_EL}")

        # Optionally wait only on those axes
        if wait:
            waits = []
            if abs(dcnt_x) >= MIN_PR_COUNTS: waits.append(f"AM {AXIS_AZ}")
            if abs(dcnt_y) >= MIN_PR_COUNTS: waits.append(f"AM {AXIS_EL}")
            if waits:
                self._cmd("; ".join(waits))
        return True

    # ---------------------------------------------------
    # MAIN MOVEMENT (axis moves only when needed)
    # ---------------------------------------------------
    def move_absolute(self, az_deg, el_sky_deg, eps_deg=1e-6):
        """Move to absolute AZ/EL_sky. Only axes that need change will move."""
        target_az = _clip(az_deg, AZ_MIN, AZ_MAX)
        target_el = _clip(el_sky_deg - 90.0, EL_MIN, EL_MAX)

        if self.sim:
            self.curr_az, self.curr_el = target_az, target_el
            self.curr_pos = [self.curr_az, self.curr_el, 0.0]
            return

        move_x = abs(target_az - self.curr_az) > eps_deg
        move_y = abs(target_el - self.curr_el) > eps_deg
        if not (move_x or move_y):
            return

        curr_cnt_x = int(round(self.curr_az * self.cnt_az))
        curr_cnt_y = int(round(self.curr_el * self.cnt_el))
        tgt_cnt_x  = int(round(target_az * self.cnt_az))
        tgt_cnt_y  = int(round(target_el * self.cnt_el))
        dcnt_x = tgt_cnt_x - curr_cnt_x
        dcnt_y = tgt_cnt_y - curr_cnt_y

        if self._queue_begin_wait(dcnt_x, dcnt_y, wait=True):
            self.curr_az = target_az
            self.curr_el = target_el
            self.curr_pos = [self.curr_az, self.curr_el, 0.0]

    def move_relative(self, d_az, d_el_sky, eps_cnt=1):
        """Relative movement (ΔAz, ΔEl_sky). Only axes with non-zero counts move."""
        d_az = _clip(d_az, -MAX_STEP_DEG, MAX_STEP_DEG)
        d_el = _clip(d_el_sky, -MAX_STEP_DEG, MAX_STEP_DEG)

        new_az = _clip(self.curr_az + d_az, AZ_MIN, AZ_MAX)
        new_el = _clip(self.curr_el + d_el, EL_MIN, EL_MAX)

        if self.sim:
            self.curr_az, self.curr_el = new_az, new_el
            self.curr_pos = [new_az, new_el, 0.0]
            return

        dcnt_az = int(np.round((new_az - self.curr_az) * self.cnt_az))
        dcnt_el = int(np.round((new_el - self.curr_el) * self.cnt_el))

        if self._queue_begin_wait(dcnt_az, dcnt_el, wait=True):
            self.curr_az, self.curr_el = new_az, new_el
            self.curr_pos = [new_az, new_el, 0.0]

    def degSteer(self, az_gim, el_gim, absolute=True, wait=False, eps_deg=1e-6, eps_cnt=1):
        """
        Steer using *gimbal-frame* degrees.
        AZ_gim: -90..+90 (0=N), EL_gim: -90..+90 (0=Up)
        - absolute=True: send PR deltas to hit absolute targets
        - absolute=False: PR by deltas (deg)
        Moves only axes that need motion (per eps).
        """
        target_az = _clip(float(az_gim), AZ_MIN, AZ_MAX)
        target_el = _clip(float(el_gim), EL_MIN, EL_MAX)

        if self.sim:
            if absolute:
                self.curr_az, self.curr_el = target_az, target_el
            else:
                self.curr_az = _clip(self.curr_az + target_az, AZ_MIN, AZ_MAX)
                self.curr_el = _clip(self.curr_el + target_el, EL_MIN, EL_MAX)
            self.curr_pos = [self.curr_az, self.curr_el, 0.0]
            return

        if absolute:
            move_x = abs(target_az - self.curr_az) > eps_deg
            move_y = abs(target_el - self.curr_el) > eps_deg
            if not (move_x or move_y):
                return

            curr_cnt_x = int(round(self.curr_az * self.cnt_az))
            curr_cnt_y = int(round(self.curr_el * self.cnt_el))
            tgt_cnt_x  = int(round(target_az * self.cnt_az))
            tgt_cnt_y  = int(round(target_el * self.cnt_el))
            dcnt_x = tgt_cnt_x - curr_cnt_x
            dcnt_y = tgt_cnt_y - curr_cnt_y

            if self._queue_begin_wait(dcnt_x, dcnt_y, wait=wait):
                self.curr_az = target_az
                self.curr_el = target_el
        else:
            # relative deltas in degrees → counts
            dcnt_az = int(round(target_az * self.cnt_az))
            dcnt_el = int(round(target_el * self.cnt_el))

            if self._queue_begin_wait(dcnt_az, dcnt_el, wait=wait):
                self.curr_az = _clip(self.curr_az + (dcnt_az / self.cnt_az), AZ_MIN, AZ_MAX)
                self.curr_el = _clip(self.curr_el + (dcnt_el / self.cnt_el), EL_MIN, EL_MAX)

        self.curr_pos = [self.curr_az, self.curr_el, 0.0]

    # ---------------------------------------------------
    # UTILITY
    # ---------------------------------------------------
    def stop(self):
        if not self.sim:
            self._cmd("ST")
        print("[STOP] Motion halted.")

    def go_home(self):
        """Return to (AZ=0, EL=0 -> Up). Only moves axes that need it."""
        self.move_absolute(0.0, 90.0)  # 90 sky = EL_gimbal 0

    def wait(self, t=0.1):
        time.sleep(t)
