from user import USERNAME, PASSWORD, TO, MESSAGE


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import time

# class InstaBot:
#     def __init__(self, username, password):
#         browserProfile = webdriver.ChromeOptions()
#         browserProfile.add_experimental_option("prefs",{'intl.accept_languages': 'en,en_US'})

#         self.browser = webdriver.Chrome('chromedriver.exe', options=browserProfile)
#         self.username = username
#         self.password = password
    
#     def sing_instagram(self):
#         self.browser.get("https://www.instagram.com/accounts/login/")
#         time.sleep(2)
#         self.browser.find_element("xpath","//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(self.username)
#         self.browser.find_element("xpath","//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(self.password)
#         self.browser.find_element("xpath","//*[@id='loginForm']/div/div[3]/button").click()
#         time.sleep(10)
    
#     def send_message(self, to,message):
        

#         self.browser.get(f"https://www.instagram.com/direct/t/{to}")
#         time.sleep(2)
#         notifications=self.browser.find_element("xpath","/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
#         if notifications.is_displayed():
#             notifications.click()
#         time.sleep(2)
#         div=self.browser.find_element("xpath","/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]")
#         div.click()
#         textarea=self.browser.find_element('xpath','//textarea[@placeholder="Message..."]')

#         textarea.click()
#         time.sleep(2)
#         textarea.send_keys(message)
#         time.sleep(1)
#         textarea.send_keys(Keys.ENTER)
#         time.sleep(10)

# user=InstaBot(USERNAME, PASSWORD)
# user.sing_instagram()
# user.send_message(TO,MESSAGE)   


class LinkedinConnectBot:
    def __init__(self, username, password):
        browserProfile = webdriver.ChromeOptions()
        browserProfile.add_experimental_option("prefs",{'intl.accept_languages': 'en,en_US'})

        self.browser = webdriver.Chrome('chromedriver.exe', options=browserProfile)
        self.browser.maximize_window()
        self.username = username
        self.password = password
    
    def sing_linkedin(self):
        self.browser.get("https://www.linkedin.com/login")
        time.sleep(2)
        self.browser.find_element("xpath","//*[@id='username']").send_keys(self.username)
        self.browser.find_element("xpath","//*[@id='password']").send_keys(self.password)
        self.browser.find_element("xpath","//*[@id='organic-div']/form/div[3]/button").click()
        time.sleep(2)
    def send_connect(self):

        self.browser.get(f"https://www.linkedin.com/mynetwork/")
        time.sleep(2)
        connects=self.browser.find_elements("xpath",".//section/div/footer/button")
        for connect in connects:
            #click button in connect dev
            span=connect.find_element("xpath",".//span")
            if span.text=="Bağlantı kur":
                connect.click()
            time.sleep(1)


        



user=LinkedinConnectBot(username=USERNAME, password=PASSWORD)
user.sing_linkedin()
user.send_connect()
