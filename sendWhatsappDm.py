import random
import string
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.service import Service

from filterNumbers import filterNumbers
from constants import *


#defining chrome options
service = Service()
chromeOptions = Options()
chromeOptions.add_argument("start-maximized")
userDataDir = ''.join(random.choices(string.ascii_letters, k=8))
chromeOptions.add_argument(f"--user-data-dir={CHROME_DATA_DIR}{userDataDir}")
chromeOptions.add_argument("--incognito")
#initializing chrome driver
browser = webdriver.Chrome(options=chromeOptions, service=service)

#opening whatsapp in max window size
browser.get(BASE_URL)
browser.maximize_window()

filterNumbers()
# input file for phone numbers

# filename = FILTERED_NUMBERS_FILE_NAME

currentDirectory = os.path.dirname(os.path.abspath(__file__))
filteredInputNumbersFile = os.path.join(currentDirectory, FILTERED_NUMBERS_FILE_NAME)
with open(filteredInputNumbersFile, "r") as file:
    filteredInputNumbersFileData = file.read()
phoneNumbers = filteredInputNumbersFileData.split("\n")

# input file for input message

# filename = INPUT_MESSAGE_FILE_NAME

inputMessageFile = os.path.join(currentDirectory,INPUT_MESSAGE_FILE_NAME)
with open(inputMessageFile, "r") as file:
    inputMessage = file.read()

if len(phoneNumbers) == 0:
    print('No phone numbers found in filteredNumbers.txt file.')
    exit()

#sending message to each phone
for phone in phoneNumbers:
    print('Sending message to:', phone)
    try:
        #opening whatsapp chat for the current number
       
        browser.get(CHAT_URL.format(phone=phone))
        time.sleep(1)

        # Wait for the input box
       
        inputBox = WebDriverWait(browser, 20).until(
            expected_conditions.presence_of_element_located((By.XPATH, inputXpath))
        )   

        # Get a list of all files in the inputFiles directory
        inputFilesDir = os.path.join(os.path.dirname(os.path.abspath(__file__)), INPUT_FILES_DIR)
        inputFilesList = os.listdir(inputFilesDir)

        if len(inputFilesList) > 0:
            #find and click attach icon
            attachmentButton = browser.find_element(By.XPATH, ATTACHMENT_BUTTON_XPATH)
            attachmentButton.click()

            # Iterate over each file and upload it
            for fileName in inputFilesList:
                filePath = os.path.join(inputFilesDir, fileName)
                fileInput = browser.find_element(By.XPATH, '//input[@type="file"]')
                fileInput.send_keys(filePath)

        #clicking send button after selecting a file
        sendButton = WebDriverWait(browser, 60).until(
            expected_conditions.presence_of_element_located((By.XPATH, SEND_BUTTON_XPATH))
        )
        sendButton.click()  
        time.sleep(1)

        #sending message 
        for line in inputMessage.split('\n'):
            inputBox.send_keys(line)
            inputBox.send_keys(Keys.SHIFT + Keys.ENTER) 
        inputBox.send_keys(Keys.ENTER)
        time.sleep(1)

    except TimeoutException as e:
        print(e.msg)
        continue

    except WebDriverException:
        continue

#Clicking menu button
menuButton = browser.find_element(By.XPATH, MENU_BUTTON_XPATH)
menuButton.click()

#clicking logout option from the menu options
logout = WebDriverWait(browser, 60).until(
        expected_conditions.presence_of_element_located((By.XPATH, LOGOUT_XPATH))
    )
logout.click()

#clicking logout confirmation
logoutConfirmation  = WebDriverWait(browser, 60).until(
        expected_conditions.presence_of_element_located((By.XPATH, LOGOUT_CONFIRMATION_XPATH))
    )
logoutConfirmation.click()

time.sleep(3)
browser.quit()

# Write the file data to a different file
outputFilename = OUTPUT_FILE_NAME
outputFile = os.path.join(currentDirectory, outputFilename)
with open(outputFile, "w") as outFile:
    outFile.write(filteredInputNumbersFileData)
    
# Delete the contents of the file
with open(filteredInputNumbersFile, "w") as file:
    file.truncate()
print('filteredNumbers.txt file data deleted.')
