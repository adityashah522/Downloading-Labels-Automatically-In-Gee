# Downloading Labels Automatically in GEE

This project provides a Python script that **automatically downloads labels from Google Earth Engine (GEE)** using Selenium.  
It was created to **save time and reduce manual effort** when working with large datasets or repetitive label downloads.

## Why This Project Exists
Working with GEE often requires downloading many labels or datasets manually, which is time-consuming and prone to errors.  
This tool automates the process, allowing researchers and developers to focus on data analysis rather than repetitive tasks.

## Features
- Logs into Google Earth Engine automatically.
- Downloads labels or datasets directly from the platform.
- Handles browser interactions using Selenium.
- Compatible with Chrome (requires ChromeDriver).

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/gee-label-downloader.git
   cd gee-label-downloader
Install the required Python packages:
pip install -r requirements.txt
Download ChromeDriver that matches your Chrome version and ensure it is in your system PATH.
Usage
Open download_labels.py in your preferred editor.
Configure your GEE credentials if needed.
Run the script:
python download_labels.py
The labels will be saved to the output folder specified in the script.
Project Structure
gee-label-downloader/
│
├── download_labels.py       # Main script
├── README.md                # Project description
├── requirements.txt         # Python dependencies
├── LICENSE                  # License file
└── .gitignore               # Files to ignore in Git
Notes
Ensure your Chrome and ChromeDriver versions match.
Avoid committing sensitive information (like credentials) to the repository.
Optional: Add screenshots or examples to improve clarity for users.
License
This project is licensed under the MIT License.
