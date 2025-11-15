#!/usr/bin/env python3
"""
TLE_Parser_Test.py — Concise output
Print SKY (Az, El) and GIMBAL (MIRROR) (Az_gimbal, El_gimbal).
- Sky frame: Az 0°=North,+90°=East; El 0°=Horizon,+90°=Up
- Gimbal frame: El_gimbal = El_sky - 90°; Az wrapped to [-180,180)
- AZ usable range: ±90°; if outside, mirror using AZ±180°, EL→-EL
"""

import datetime
from pathlib import Path
from skyfield.api import load, wgs84

# ---------------- USER SETTINGS ----------------
SAT_NAME = "ASIASAT 5"
GS_LAT = 1.2966
GS_LON = 103.7764
GS_ALT_M = 30
# -----------------------------------------------

def _wrap180(deg):
    return ((deg + 180.0) % 360.0) - 180.0

def main():
    # Load today's TLE file
    today = datetime.date.today()
    tle_dir = Path(__file__).parent / "TLE"
    tle_path = tle_dir / f"TLE{today}.tle"
    if not tle_path.exists():
        raise FileNotFoundError(f"TLE file not found: {tle_path}")

    # Load satellite
    sats = load.tle_file(str(tle_path))
    sat = next((s for s in sats if s.name.strip().upper() == SAT_NAME.strip().upper()), None)
    if sat is None:
        print(f"[ERROR] '{SAT_NAME}' not in {tle_path.name}")
        return

    # Compute sky position (now)
    ts = load.timescale()
    gs = wgs84.latlon(GS_LAT, GS_LON, elevation_m=GS_ALT_M)
    alt, az, _ = (sat - gs).at(ts.now()).altaz()

    az_sky = az.degrees
    el_sky = alt.degrees

    # Convert to gimbal frame
    el_gimbal = el_sky - 90.0
    az_wrapped = _wrap180(az_sky)

    # If AZ outside ±90°, mirror to bring into range and flip EL
    if -90.0 <= az_wrapped <= 90.0:
        az_mirror = az_wrapped
        el_mirror = el_gimbal
    else:
        az_mirror = _wrap180(az_wrapped - 180.0) if az_wrapped > 90.0 else _wrap180(az_wrapped + 180.0)
        el_mirror = -el_gimbal

    # --- Minimal labeled output ---
    print(f"SKY:     AZ={az_sky:.2f}°, EL={el_sky:.2f}°")
    print(f"GIMBAL:  AZ={az_mirror:.2f}°, EL={el_mirror:.2f}°  (MIRROR)")

if __name__ == "__main__":
    main()
