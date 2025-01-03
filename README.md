# DIY Raspberry Pi Radio with Scheduled Playlists

A simple project to build a radio using a Raspberry Pi that plays custom playlists at scheduled times (e.g., morning and evening). The setup supports audio playback in headless mode (no GUI) using VLC.

---

## Features
- Plays custom playlists based on the time of day.
- Supports headless operation using VLC media player.
- Configurable via Python scripts.
- Works with Raspberry Pi (Model 1, 4, Zero, etc.).

---

## Requirements
### Hardware
- Raspberry Pi (any model with audio output).
- Power supply, speakers (3.5mm, USB, or amplifier).
- RTC module (DS3231) for accurate scheduling.
- MicroSD card (8GB or higher).

### Software
- Raspberry Pi OS (Lite or Desktop).
- VLC media player for audio playback.
- Python 3 with required libraries.

---

## Setup

### 1. Hardware Connections
- Connect RTC to the Raspberry Pi:
  - `VCC → 3.3V`, `GND → GND`, `SDA → GPIO2`, `SCL → GPIO3`.
- Audio Output Options:
  - **3.5mm Jack**: Plug directly into speakers.
  - **USB Sound Card**: Use `cvlc` to configure.
  - **Amplifier + Speaker**: Connect via GPIO pins (PWM output).

---

### 2. Install Dependencies
```bash
sudo apt update && sudo apt install vlc alsa-utils python3-pip
