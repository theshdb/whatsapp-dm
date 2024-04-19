BASE_URL = "https://web.whatsapp.com/"

CHROME_DATA_DIR = "/tmp/chrome-data/"

INPUT_FILES_DIR = "inputFiles"

INPUT_MESSAGE_FILE_NAME = "inputMessage.txt"

CHAT_URL = "https://web.whatsapp.com/send?phone={phone}&text&type=phone_number&app_absent=1"

INPUT_XPATH = '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div[2]/div[1]/p'
        
FILTERED_NUMBERS_FILE_NAME = "filteredNumbers.txt"

OUTPUT_FILE_NAME = "messageSentToNumbers.txt"

ATTACHMENT_BUTTON_XPATH = '//div[@title="Attach"]'

SEND_BUTTON_XPATH = '//*[@id="app"]/div/div[2]/div[2]/div[2]/span/div/span/div/div/div[2]/div/div[2]/div[2]/div/div[1]/span'

MENU_BUTTON_XPATH = '//div[@role="button"][@title="Menu"]'

LOGOUT_XPATH = '//div[@aria-label="Log out"]' 
# or //*[@id="app"]/div/div[2]/div[3]/header/div[2]/div/span/div[5]/span/div/ul/li[6]/div

LOGOUT_CONFIRMATION_XPATH = '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[3]/div/button[2]/div/div'