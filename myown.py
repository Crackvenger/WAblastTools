
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import pandas
import keyboard as key

excel_data = pandas.read_excel('Recipients data.xls', sheet_name='Recipients')

count = 0

driver = webdriver.Chrome("./chromedriver.exe")
driver.get('https://web.whatsapp.com')
input("Press ENTER after login into Whatsapp Web and your chats are visiable.")

for column in excel_data['Contact'].tolist():
    try:
        url = 'https://web.whatsapp.com/send?phone=' + '+62' + str(excel_data['Contact'][count]) + '&text=' + excel_data['Message'][0]

        driver.get(url)
        sleep(10)
        hit_enter = ActionChains(driver)
        hit_enter.send_keys(Keys.ENTER)
        hit_enter.perform()
        sleep(5)
        print('Message sent to: ' + str(excel_data['Contact'][count]))
        count += 1
    except Exception as e:
        print('Failed to send message to ' +
              str(excel_data['Contact'][count]) + str(e))
driver.quit()
print("The script executed successfully.")


