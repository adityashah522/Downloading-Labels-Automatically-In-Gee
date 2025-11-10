# Controlling Chrome Browser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



# For waiting between actions
from time import sleep


# For checking google drive
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

# Opening up Chrome to GEE
chromedriverlocation = "./chromedriver"
service = Service(chromedriverlocation)

options = Options()
options.add_argument(r'--user-data-dir=/Users/adityashah/Desktop/GEE_Auto/automation_profile')

options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(options=options, service=service)
driver.get("https://code.earthengine.google.com/")


cont = input("Press enter to countinue: ")


studyareanumber = int(input("Enter Study Area Number to Start:"))

xpathdivnumber = int(input("Enter the final div indentifer from the Xpath:"))


# To scroll to the study area
def scroll(divnumber):
    element = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[1]/div/div[1]/div/div[1]/div/ee-tab-panel/ee-tab[1]/div/div[3]/ee-zippy/div[2]/div[1]/div/div[2]/div/div/div['+str(divnumber)+']')
    ActionChains(driver).scroll_to_element(element).perform()
    sleep(5.0)
    print("done scroll")
    element.click()
    print("studyarea in")

# To run the scrpit which will send a task to download the .tif file of the label
def run_scrpit():
    runscrpit = driver.find_element(By.XPATH, '//*[@id="main"]/div[2]/div[1]/div/div[1]/div/div[2]/div/div[1]/div/button[3]')
    runscrpit.click()
    print("done runscrpit")


# To go to the task tab where the task was created
def go_to_task_tab():
    upper_shadow1_1 = driver.find_element(By.CSS_SELECTOR, '#main > div.goog-splitpane > div.goog-splitpane-first-container > div > div.goog-splitpane-second-container > div > ee-tab-panel')
    uppershadow_exct1_1 = upper_shadow1_1.shadow_root
    gototask = uppershadow_exct1_1.find_element(By.CSS_SELECTOR, 'div > button:nth-child(3)')
    gototask.click()
    print("done go to task")

# To open uo the prompt to download the file 
def run_download_file():
    wdw(driver, 20).until(
        lambda d: d.execute_script("""
            const taskPane = document.querySelector('ee-task-pane');
            if (!taskPane) return false;
            const eeButton = taskPane.shadowRoot.querySelector('ee-button');
            if (!eeButton) return false;
            const paperButton = eeButton.shadowRoot.querySelector('paper-button');
            return paperButton !== null;
        """)
    )

    rundownloadfile = driver.execute_script("return document.querySelector('ee-task-pane').shadowRoot.querySelector('ee-button')")
 
    rundownloadfile.click()
    print("done go to download")

# Change the name of the file that will be downloaded
def place_to_change_file_name(new_value=""):
    wdw(driver, 20).until(
        lambda d: d.execute_script("""
            const input = document.querySelector('ee-destination-input')
                .shadowRoot.querySelector('paper-input.drive-file-name-prefix')
                .shadowRoot.querySelector('input');
            return input !== null;
        """)
    )

    driver.execute_script(f"""
        const input = document.querySelector('ee-destination-input')
            .shadowRoot.querySelector('paper-input.drive-file-name-prefix')
            .shadowRoot.querySelector('input');
        if (input) {{
            input.value = '{new_value}';  // clear or set new value
            input.dispatchEvent(new Event('input', {{ bubbles: true }})); // trigger input event
        }}
    """)

    print("done place to change file")

    
# Will run the download task
def send_to_download():
    wdw(driver, 20).until(
        lambda d: d.execute_script("""
            const dialog = document.querySelector('ee-image-config-dialog');
            if (!dialog) return false;
            const eeDialog = dialog.shadowRoot.querySelector('ee-dialog');
            if (!eeDialog) return false;
            const okButton = eeDialog.shadowRoot.querySelector('ee-button.ok-button');
            if (!okButton) return false;
            const paperBtn = okButton.shadowRoot.querySelector('paper-button');
            return paperBtn !== null;
        """)
    )

 
    driver.execute_script("""
        return document.querySelector('ee-image-config-dialog')
            .shadowRoot.querySelector('ee-dialog')
            .shadowRoot.querySelector('ee-button.ok-button')
            .shadowRoot.querySelector('paper-button').click();
    """)
    print("done send to download")

# Google Drive Authentification
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
gauth.http_timeout = (3600)
drive = GoogleDrive(gauth)

folderid = str(input('Enter your folder ID: '))
# '1dB8rpQ76aHJY99XKnbhgP81yiUD8yY8W'

# Loop to run the scrpit
# Change the range for the amount of study areas you need
for i in range(86,100):
    scroll(xpathdivnumber)
    sleep(3.0)
    go_to_task_tab()
    sleep(3.0)
    run_scrpit()
    sleep(3.0)
    run_download_file()
    sleep(3.0)
    place_to_change_file_name("studyarea"+str(studyareanumber))
    sleep(3.0)


    studyareanumber = int(studyareanumber)

    send_to_download()
    print("downloading")

    found = False

    while not found:
        file_list = drive.ListFile({'q': f"'{folderid}' in parents and trashed=false"}).GetList()

        for file in file_list:
            if file["title"] == ("studyarea" + str(studyareanumber)+'.tif'):
                print("Found File")
                found = True
        if not found:
            sleep(60.0)
            print("waiting")

    studyareanumber = (int(studyareanumber)) + 1
    xpathdivnumber = int(xpathdivnumber) + 1


driver.quit()  
print("All done")