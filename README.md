# DLP-Printer (Raspberry Pi + Stepper Motor + Full-Screen Image Projection)

This repository is a DLP 3D-printer control stack built around Raspberry Pi nodes.
It coordinates:

- stepper motor motion (X/Y, slice stepping),
- projector/image exposure timing (full-screen image flashes),
- sensor/calibration logic, and
- TCP/serial communication between host and printer nodes.

## What the code does

The codebase has four parts:

1. **Raspberry Pi slave controller (Python)** in `code/scripts/`
2. **Earlier Python prototypes** in `code/old/` and `legacy code/Python/`
3. **Windows host GUI/controller (C#)** in `legacy code/3DSPrinter/`
4. **Arduino motor firmware** in `legacy code/ArduinoCode/`

Together, these components run a layer-by-layer print cycle:

1. move platform/motors,
2. display a bright slice image full-screen on one or more projectors,
3. wait for exposure time,
4. blank the screen,
5. repeat.

---

## Main Raspberry Pi runtime (current Python path)

### 1) TCP command receiver (`code/scripts/slave.py`)

- Starts a TCP server on the Pi’s local IP and listens on `constants.TCP_PORT`.
- Accepts command packets from a client and decodes them into a message struct.
- Passes decoded instructions to `ThreadManager`.
- Handles graceful shutdown with GPIO cleanup.

### 2) Command format (`code/scripts/devices/message_structure.py`)

Messages are encoded with a simple framed protocol:

- Starts with `#` (instruction) or `@` (feedback)
- Ends with `!`
- Comma-separated payload fields:
  - `motor_id`
  - `instruction`
  - `distance_travel`
  - `direction`
  - `sensor_on`
  - `resolution`
  - `exposure_time`
  - `img_file`

Example shape:

`#<motor_id>,<instruction>,<distance>,<direction>,<sensor>,<resolution>,<exposure>,<image>!`

### 3) Instruction dispatch (`code/scripts/devices/threadManager.py`)

- Creates motor and sensor worker threads in slave mode.
- Routes instructions by `motor_id` (or `0` for broadcast/all motors).
- Handles instruction categories including:
  - motor stop,
  - sensor calibration,
  - motor/image flash operations,
  - optional sensor-engaged motion bounds checks.

### 4) Startup scripts (`code/start1.sh.t`, `code/start2.sh.t`)

These launch Pi slave instances with a motor ID argument (`1` or `2`):

- `sudo python .../code/scripts/slave.py 1`
- `sudo python .../code/scripts/slave.py 2`

---

## Full-screen image flashing / projection logic

Projection behavior is implemented in `legacy code/Python/printer.py`:

- Opens full-screen OpenCV windows for projector outputs.
- Moves windows to specific monitor offsets.
- Alternates between `blank.jpg` and print slice image (`square.jpg` in sample).
- Waits for exposure (`cv2.waitKey(delayMs)`), then blanks again.

There is also monitor management in `legacy code/3DSPrinter/SerialPortCommunication/MonitorManager.cs`:

- Creates borderless full-screen windows on one or more monitors.
- Swaps projector background image between print and blank states.

---

## Stepper motor control path

### Arduino firmware

`legacy code/ArduinoCode/MotorControl/MotorControl.ino` parses serial commands such as:

- `G0` / `G1` for speed mode,
- `X...` and `Y...` axis movements,
- signed values for direction.

It drives pulse/direction/enable pins and replies with `OK` when movement is complete.

### Host-side serial control

- `legacy code/Python/printer.py` and `printer2.py` send movement commands over serial.
- `legacy code/3DSPrinter/SerialPortCommunication/CommunicationManager.cs` and UI in `3DSPrinter.cs` perform similar serial command/ack flow from Windows.

---

## Sensor and Pi GPIO elements

- `code/scripts/__init__.py` and `code/old/sensor.py` contain RC timing / GPIO logic (`RPi.GPIO`).
- The project includes Adafruit libraries under `code/scripts/devices/adafruit/` (ADS/I2C support).
- `threadManager.py` references `SensorThread` calibration and position checks.

---

## Important repository notes

1. **Some critical runtime modules are only present as `.pyc` files** (for example motor/sensor thread implementations and constants in `code/scripts/`).
  - Source for those modules is not included, so behavior must be recovered from bytecode or reimplemented.
2. Most Python code targets **Python 2 era** conventions, with partial Python 3 migration in some files.
3. Multiple generations coexist; not every folder is part of one single executable pipeline.

---

## End-to-end architecture

- A host (Windows app or Python script) orchestrates print settings and timing.
- Commands are sent over TCP to one or more Raspberry Pi slave nodes.
- Each Pi slave decodes command packets, dispatches motor/sensor/image tasks via worker threads.
- Motor movement is executed through stepper drivers and/or serial-connected microcontroller firmware.
- Projectors display layer masks in full-screen, then blank between slices.

---

## Running this project today

Before bring-up, complete these steps:

1. recover/decompile or re-implement missing `.py` sources from `.pyc`,
2. normalize on one Python version (prefer Python 3),
3. reconstruct `constants` values (TCP port, instruction IDs, slave IPs),
4. validate GPIO pin mapping and motor driver wiring,
5. verify projector monitor layout and image path handling,
6. test serial command compatibility with Arduino firmware.

Because this controls motors and UV/light exposure hardware, test with power limits and safety interlocks before full operation.
