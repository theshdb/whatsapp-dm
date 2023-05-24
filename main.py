# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time

# # Create instance of Chrome webdriver
# driver = webdriver.Chrome()

# # Open WhatsApp URL in Chrome browser
# driver.get("https://web.whatsapp.com/")

# # Wait for user to scan QR code
# input("Please scan QR code and then press enter")

# # Find the chat search field and enter the unsaved phone number
# chat_search = driver.find_element("xpath", '//input[@class="_2_1wd copyable-text selectable-text"]')
# chat_search.click()
# chat_search.send_keys("+919701446690")
# chat_search.send_keys(Keys.ENTER)

# # Wait for chat to load
# time.sleep(2)

# # Find the chat message input field and enter the message
# chat_message = driver.find_element("xpath", '//div[@class="_3uMse"][@contenteditable="true"]')
# chat_message.click()
# chat_message.send_keys("Your message goes here")
# chat_message.send_keys(Keys.ENTER)

# # Close the browser
# driver.quit()













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

BASE_URL = "https://web.whatsapp.com/"
CHAT_URL = "https://web.whatsapp.com/send?phone={phone}&text&type=phone_number&app_absent=1"

chrome_options = Options()
chrome_options.add_argument("start-maximized")
user_data_dir = ''.join(random.choices(string.ascii_letters, k=8))
chrome_options.add_argument("--user-data-dir=/tmp/chrome-data/" + user_data_dir)
chrome_options.add_argument("--incognito")

browser = webdriver.Chrome(ChromeDriverManager().install(),  options=chrome_options,)

browser.get(BASE_URL)
browser.maximize_window()


phone = "6302617310"
message = 'Hi There. This is test message from PythonCircle.com'


browser.get(CHAT_URL.format(phone=phone))
time.sleep(3)


inp_xpath = (
    '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
)
input_box = WebDriverWait(browser, 60).until(
    expected_conditions.presence_of_element_located((By.XPATH, inp_xpath))
)

input_box.send_keys(message)
input_box.send_keys(Keys.ENTER)

time.sleep(10)


