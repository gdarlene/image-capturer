# Image Capture and Upload

## Overview
This project captures images from a specified folder and uploads them to a remote server using `curl`. It is designed to redudancy by moving uploaded images to a separate folder.

## Features
- Monitors a designated folder for new images.
- Uploads images to a specified URL.
- Moves uploaded images to a different folder to avoid duplication.
- Supports continuous monitoring with a configurable check interval.

## Requirements
- Python 3.x
- Required libraries:
  - `os`
  - `time`
  - `subprocess`
  - `shutil`
  - `curl` (ensure it's installed and accessible from the command line)

## Setup
1. Clone the repository or download the project files.
2. Navigate to the project directory:
   ```bash
   cd path/to/your/project
3.Create a virtual environment:
python -m venv .venv

4.Activate the vm for running the python codes
(windows: .venv\Scripts\activate)
