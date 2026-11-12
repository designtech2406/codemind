# Code Mind – ESP32 Room Monitor

Reads a DHT22 sensor and serves live temperature and humidity on a web page hosted by the ESP32.

## Wiring

| DHT22 pin | ESP32 pin   |
|-----------|-------------|
| + (VCC)   | 3V3         |
| OUT (Data)| GPIO 4 (D4) |
| - (GND)   | GND         |

## Setup

1. Install the **DHT sensor library** (Adafruit) in the Arduino IDE.
2. In `room_monitor/room_monitor.mp3/`, copy `secrets.example.h` to `secrets.h` and enter your Wi-Fi SSID and password.
3. Open `room_monitor.mp3.ino`, select your ESP32 board, and upload.
4. Open the Serial Monitor (115200 baud) to find the IP address, then open `http://<ip>` on your phone.
