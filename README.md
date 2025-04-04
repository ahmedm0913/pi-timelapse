# Raspberry Pi Timelapse Camera Project

## Features
- Automated timelapse capture
- Press 'q' to stop recording
- Saves organized frames and videos

## Setup
```bash
sudo apt install python3-picamera2 ffmpeg python3-opencv
pip3 install -r requirements.txt
```
## Usage
```bash
python3 timelapse.py
```
---
## Project Structure
Timelapse/
|--'Folders with Images and Video'
|--timelapse.py		# Main Script
|--requirements.txt	# Dependancies	
|--README.md

##Troubleshooting
- If camera isn't detected:
```bash
sudo raspi-config 	#Enable Camera under Interface options
```
---

