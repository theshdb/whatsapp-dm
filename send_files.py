import random
import string
import time
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

BASE_URL = "https://web.whatsapp.com/"

#defining chrome options
chrome_options = Options()
chrome_options.add_argument("start-maximized")
user_data_dir = ''.join(random.choices(string.ascii_letters, k=8))
chrome_options.add_argument("--user-data-dir=/tmp/chrome-data/" + user_data_dir)
chrome_options.add_argument("--incognito")

#initializing chrome driver
browser = webdriver.Chrome(ChromeDriverManager().install(),  options=chrome_options,)

#opening whatsapp in max window size
browser.get(BASE_URL)
browser.maximize_window()

file_path = '/Users/theshdb/Documents/Jaffer/clean_numbers.txt'

with open(file_path, "r") as file:
    file_content = file.read()

phones = file_content.split("\n")
# phones = ['+916302617310', '9246828819', '9701446690']

# Defining the lines of message
lines = [
    "Open plots for sale @ vikarabad main road, by RIDGE.",
    "- best investment opportunity, @ vikarabad main road.",
    "- DTCP government approved plots.",
    "- Plot price starts with, 5000 per sq yard.",
    "- for more information",
    "Contact- 9121830512"
]

#sending message to each phone
for phone in phones:
    print(phone)
    try:
        #opening whatsapp chat for the current number
        CHAT_URL = "https://web.whatsapp.com/send?phone={phone}&text&type=phone_number&app_absent=1"
        browser.get(CHAT_URL.format(phone=phone))
        time.sleep(1)
        # Wait for the input box
        inp_xpath = (
            '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
        )
        input_box = WebDriverWait(browser, 20).until(
            expected_conditions.presence_of_element_located((By.XPATH, inp_xpath))
        )

        #find and click attach icon
        attachment_button = browser.find_element(By.XPATH, '//div[@title="Attach"]')
        attachment_button.click()

        #sending a file
        file_input = browser.find_element(By.XPATH, '//input[@type="file"]')
        file_input.send_keys('/Users/theshdb/Documents/Jaffer/Ridge.pdf') 

        #clicking send button after selecting a file
        send_button = WebDriverWait(browser, 60).until(
            expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[3]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div/span'))
        )
        send_button.click()
        time.sleep(1)
        #sendign message 
        for line in lines:
            input_box.send_keys(line)
            input_box.send_keys(Keys.SHIFT + Keys.ENTER) 
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)

    except TimeoutException as e:
        print(e.msg)
        continue

    except WebDriverException:
        continue

   

#Clicking menu button
menu_button = browser.find_element(By.XPATH, '//div[@role="button"][@title="Menu"]')
menu_button.click()

#clicking logout option from the menu options
logout = WebDriverWait(browser, 60).until(
        expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[4]/header/div[2]/div/span/div[4]/span/div/ul/li[6]'))
    )
logout.click()

#clicking logout confirmation
logout_confirmation  = WebDriverWait(browser, 60).until(
        expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[3]/div/button[2]/div/div'))
    )
logout_confirmation.click()
print('Logged out')

time.sleep(3)
# Close the browser
browser.quit()









