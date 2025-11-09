# Downloading Labels Automatically in GEE

This project is a **web automation bot** that automates downloading labeled study areas from **Google Earth Engine (GEE)** and saves them directly to **Google Drive**. It is built with **Python**, **Selenium**, and **PyDrive2**.

---

## Features

- Automatically scrolls through GEE to select study areas.
- Navigates tabs and runs scripts to generate outputs.
- Downloads files to Google Drive and renames them automatically.
- Waits for files to appear in the Drive folder before proceeding.
- Handles nested **shadow DOM elements** in GEE.

---

## Technologies

- Python 3  
- Selenium WebDriver for browser automation  
- PyDrive2 for Google Drive interaction  
- ChromeDriver for controlling Chrome  
- ActionChains and JavaScript for advanced interactions  

---

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/gee-download-bot.git
   cd gee-download-bot
2. **Install dependencies:**
   ```bash
   pip install selenium pydrive2
3. **Download ChromeDriver compatible with your Chrome version and place it in the project directory.**
4. **Set Chrome profile path in the script:**
   ```python
   options.add_argument('--user-data-dir=/path/to/your/chrome/profile')
5. **Authenticate with Google Drive when prompted by PyDrive2.**
6. **Set target Google Drive folder ID in the script:**
   ```python
   folderid = 'YOUR_FOLDER_ID'

---

##Usage

**Run the script:**
```bash
python gee_auto.py
```
**The bot will:**
1. Scroll through the GEE interface.
2. Run scripts for each study area.
3. Rename and download files to Google Drive.
4. Wait until each file appears before moving to the next.

---
## Notes
This is not an AI agent; it performs predefined automation tasks.
Ensure your ChromeDriver matches your Chrome browser version.
Designed for research and educational purposes in GEE workflows.

---

## License
This project is licensed under the MIT License.







