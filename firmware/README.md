# Firmware

This folder contains embedded firmware for the wearable kyphosis monitoring system.

## Project Structure

esp32_sensor_acquisition/
├── platformio.ini
└── src/
    └── main.cpp

---

## Overview

The firmware runs on an ESP32 and is responsible for:

- Reading multi-channel EMG sensor data
- Acquiring motion data from MPU6050 sensors
- Streaming sensor data via Serial for analysis

---

## Features

- 6-channel EMG data acquisition
- Dual MPU6050 support (accelerometer + gyroscope)
- Real-time serial data output
- Designed for integration with offline signal processing

---

## Hardware Connections

| Component        | Description                      |
|----------------|----------------------------------|
| EMG Sensors     | Muscle activity measurement      |
| MPU6050         | Orientation and motion tracking  |
| ESP32           | Main controller                  |
| Vibration Motor | Feedback mechanism               |

---

## Notes

- Data collected via Serial Monitor was processed using Python scripts in the `signal-processing/` folder
- This firmware focuses on data acquisition rather than onboard processing
- Dual MPU6050 requires different I2C addresses (AD0 pin configuration)
