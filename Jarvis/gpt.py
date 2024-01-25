# Import necessary packages
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


import pathlib
ScriptDir =pathlib.Path().absolute()

url = "https://flowgpt.com/chat"
chrome_options = Options()

user_agent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2"
chrome_options.add_argument(f"user-agent={user_agent}")
chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_argument(f'user-data-dir={ScriptDir}\\chromedata')
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()
driver.get(url=url)
sleep(5)

def Websiteopener():
    while True:
        try:
            xPATH= '/html/body/div[1]/main/div[3]/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/textarea'
            driver.find_element(by=By.XPATH,value=xPATH)
            break
        except:
            pass

# def Popupremover():
#     Xpath ='/html/body/div[3]/div[3]/div/section/div/div[3]/button[2]'
#     driver.find_element(by=By.XPATH,value=Xpath).click()   
# Popupremover()
# sleep(5000)

Websiteopener()
print("Loaded")

