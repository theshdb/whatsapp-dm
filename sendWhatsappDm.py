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

BASE_URL = "https://web.whatsapp.com/"

#defining chrome options
service = Service()
chromeOptions = Options()
chromeOptions.add_argument("start-maximized")
userDataDir = ''.join(random.choices(string.ascii_letters, k=8))
chromeOptions.add_argument("--user-data-dir=/tmp/chrome-data/" + userDataDir)
chromeOptions.add_argument("--incognito")
#initializing chrome driver
browser = webdriver.Chrome(options=chromeOptions, service=service)

#opening whatsapp in max window size
browser.get(BASE_URL)
browser.maximize_window()

filterNumbers()
# input file for phone numbers
filename = 'filteredNumbers.txt'
currentDirectory = os.path.dirname(os.path.abspath(__file__))
filteredInputNumbersFile = os.path.join(currentDirectory, filename)
with open(filteredInputNumbersFile, "r") as file:
    filteredInputNumbersFileData = file.read()
phoneNumbers = filteredInputNumbersFileData.split("\n")

# input file for input message
filename = 'inputMessage.txt'
inputMessageFile = os.path.join(currentDirectory, filename)
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
        CHAT_URL = "https://web.whatsapp.com/send?phone={phone}&text&type=phone_number&app_absent=1"
        browser.get(CHAT_URL.format(phone=phone))
        time.sleep(1)

        # Wait for the input box
        inputXpath = (
            '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p'
        )
        inputBox = WebDriverWait(browser, 20).until(
            expected_conditions.presence_of_element_located((By.XPATH, inputXpath))
        )   

        # Get a list of all files in the inputFiles directory
        inputFilesDir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'inputFiles')
        inputFilesList = os.listdir(inputFilesDir)

        if len(inputFilesList) > 0:
            #find and click attach icon
            attachmentButton = browser.find_element(By.XPATH, '//div[@title="Attach"]')
            attachmentButton.click()

            # Iterate over each file and upload it
            for fileName in inputFilesList:
                filePath = os.path.join(inputFilesDir, fileName)
                fileInput = browser.find_element(By.XPATH, '//input[@type="file"]')
                fileInput.send_keys(filePath)

        #clicking send button after selecting a file
        sendButton = WebDriverWait(browser, 60).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div[1]/span'))
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
menuButton = browser.find_element(By.XPATH, '//div[@role="button"][@title="Menu"]')
menuButton.click()

#clicking logout option from the menu options
logout = WebDriverWait(browser, 60).until(
        expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div[2]/div[3]/header/div[2]/div/span/div[5]/span/div/ul/li[6]'))
    )
logout.click()

#clicking logout confirmation
logoutConfirmation  = WebDriverWait(browser, 60).until(
        expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[3]/div/button[2]/div/div'))
    )
logoutConfirmation.click()

time.sleep(3)
browser.quit()

# Write the file data to a different file
outputFilename = 'messageSentToNumbers.txt'
outputFile = os.path.join(currentDirectory, outputFilename)
with open(outputFile, "w") as outFile:
    outFile.write(filteredInputNumbersFileData)
    
# Delete the contents of the file
with open(filteredInputNumbersFile, "w") as file:
    file.truncate()
print('filteredNumbers.txt file data deleted.')






