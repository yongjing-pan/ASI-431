---
title: Global Positioning System 
parent: Individual Contributions
nav_order: 4
permalink: /GPS/
---


<div style="display:flex">
  <img src="{{site.baseurl}}/assets/images/profiles/jg.jpg" alt="Hang Jin Guang" width="200" style="border-radius:50%">
  <div style="margin-left: 20px">
    <h2>Global Positioning System </h2>
  </div>
</div>


[**3\. Global Positioning System	2**](#3.-global-positioning-system)

[2.1 Objective	2](#3.1-objective)

[2.2 Design Specifications	2](#3.2-design-specifications)

[2.3 Code Required	3](#3.3-code-required)

# **3\. Global Positioning System**  {#3.-global-positioning-system}

## **3.1 Objective** {#3.1-objective}

The integration of a Global Positioning System (GPS) module within the ground station is essential to provide accurate real-time position and heading information for satellite tracking operations. The GPS module enables precise computation of azimuth and elevation angles, which are required to continuously align the gimbal-mounted antenna with the target satellite.

As part of the ground station development, the objective of this work is to implement, calibrate, and verify a GPS-based positioning subsystem that interfaces directly with the gimbal control software and the orbital prediction module. This integration ensures that the ground station can maintain consistent tracking accuracy, even when deployed in different locations, by dynamically updating positional data.

The GPS subsystem also contributes to time synchronization for satellite pass prediction and data logging, thereby enhancing the overall reliability and autonomy of the ground station system.

## **3.2 Design Specifications**  {#3.2-design-specifications}

The Global Positioning System (GPS) module shall fulfil the following design requirements to ensure accurate and reliable position and heading determination for satellite tracking operations:

* **GPS Module:** AS-STARTKIT-HEAD-L1L2-NH-00

* **Heading Accuracy:** \< 0.2°

* **Position Accuracy:** Within ±2.5 m

* **Update Rate:** Minimum 10 Hz to support real-time gimbal motion updates

* **Communication Interface:** Serial (UART) connection to the main control unit

* **Power Supply:** 5 V DC regulated input

* **Integration Requirement:** Must interface seamlessly with the TLE parsing and gimbal control subsystems for continuous azimuth and elevation computation.

The selected GPS module meets the above specifications, providing dual-frequency L1/L2 capability for improved heading precision and resistance to multipath errors. These specifications collectively ensure stable and accurate satellite tracking performance in mobile ground station configurations.

## **3.3 Code Required** {#3.3-code-required}

The GPS data acquisition and validation were implemented in Python.  
The serial port verification script (`check_ports.py`) and the GPS parsing and heading computation module (`gps_reader.py`) are provided in **Annex C** for reference.

A. `check_ports.py` — Serial Port Discovery & Sanity Check  
Purpose

Provides a quick way to (i) list all available serial ports on the host machine and (ii) verify that the target GPS device/port can be opened at the expected settings (baud rate, timeout). This is used before running the live GPS reader to avoid silent connection failures.

Key Components

* **Port enumeration:** Uses `serial.tools.list_ports.comports()` to print detected ports and human-readable descriptions.

* **Connection probe:** Attempts to open a **candidate list** of device names for Windows (`"COM6"` and the escaped `"\\.\COM6"`) at **38400 baud** with a **2 s** timeout.

* **Result reporting:** Prints “Opened OK” / “Open failed” with the exception text to aid troubleshooting.

Inputs / Parameters

* `target = "COM6"` — change to match the actual GPS port.

* `baud = 38400` (fixed in code) — must match the GPS module’s configured baud rate.

Outputs

* Console log listing ports and the success/failure of opening each candidate device.

Typical Use

Run once after (re)plugging the GPS to confirm the correct COM name and permissions before starting higher-level scripts.

B. `gps_reader.py` — UBX-First GPS Fix & Heading Utility  
Purpose

Acquire a **single high-quality GPS fix** (time, latitude, longitude, altitude) and, when available, a **dual-antenna heading** with associated accuracy. Prioritises **u-blox UBX** messages for robustness and falls back to **NMEA** if needed. Also provides a **live status streamer** for real-time monitoring.

External Dependencies

* `pyserial` (serial I/O)

* `pyubx2` (parsing u-blox UBX protocol)

Module Structure

1\) Helper Converters

* `_auto_deg(v)` and `_auto_alt_m(h)`

  * Auto-scale raw UBX integer fields (e.g., `1e-7 deg` for lat/lon, millimetres to metres for height).

* `_auto_heading_deg(rh, ah)`

  * Scales UBX **relative heading** and **heading accuracy** (from `1e-5 deg`), then normalises heading with a `–90°` frame adjustment to align with the project’s heading convention.

* `_dm_to_deg(dm, hemi)`

  * Converts NMEA “degrees+minutes” strings into signed decimal degrees using hemisphere flags.

2\) Public API

* `read_once(port="COM6", baud=38400, max_wait_s=8.0, want_heading=True, extra_heading_wait_s=2.0)`

  * **Goal:** Return one consolidated fix as a Python dict:  
     `{time_utc, lat, lon, alt_m, heading_deg, heading_acc_deg, source}`.

  * **Acquisition strategy:**

    1. **Prefer UBX** `NAV-PVT` for position & time (requires `fixType ≥ 2`).

    2. **Listen opportunistically** for UBX `NAV-RELPOSNED` to obtain **dual-antenna heading** and its accuracy.

    3. **Fallback to NMEA** (`GGA` or `GLL`) for position if UBX is not yet available within the wait window.

    4. If position is obtained but heading is missing, keep listening up to `extra_heading_wait_s` for a late `RELPOSNED`.

  * **Timeout behaviour:** Raises `TimeoutError` if no position is acquired before `max_wait_s`.

  * **Source flag:** Sets `source = "UBX"`, `"NMEA-GGA"`, or `"NMEA-GLL"` to document where the fix came from.

* `stream_status(port="COM6", baud=38400, timeout=1.0)`

  * **Live console monitor** for continuous UBX telemetry.

  * Prints fix type (e.g., “2D/3D”), satellite count, position, altitude, and (when available) **heading with ±accuracy**.

  * Useful for antenna placement tests, sky-view diagnostics, and verifying heading stability against your **\< 0.2°** requirement.

3\) Command-Line Entry Point

When executed directly:

1. Lists available ports; 2\) Calls `read_once(...)`; 3\) Prints a formatted “GPS FIX” summary; 4\) (Optionally) enables `stream_status(...)` for continuous monitoring.

Data & Accuracy Notes

* **Heading source:** Relies on UBX `NAV-RELPOSNED` (dual-antenna/RTK-capable receivers) to obtain **true heading** and a manufacturer-reported **heading accuracy** (`heading_acc_deg`). This field can be checked programmatically against your **spec target of \< 0.2°** to gate downstream operations.

* **Time handling:** Prefers UBX-validated time; on NMEA fallback, constructs a UTC timestamp from sentence fields for logging consistency.

* **Units & normalisation:** All lat/lon in **decimal degrees**, altitude in **metres**, heading in **degrees 0–360** after the internal `–90°` convention shift (keeps your gimbal math consistent across sources).

Typical Use in the System

1. **Bring-up:** Use `check_ports.py` to confirm COM assignment.

2. **Single-fix acquisition:** Call `read_once(...)` from the tracking stack to seed ground-station location/time (and heading if available).

3. **Live QA:** Run `stream_status(...)` to evaluate antenna placement and confirm that **heading ± accuracy** meets operational thresholds before a satellite pass.