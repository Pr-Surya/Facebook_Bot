from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import random
import keyboard


XPATH = "xpath"

class FacebookBot:
    def __init__(self, email, password):
        self.browser = webdriver.Chrome()
        self.email = email
        self.password = password
    
    def signIn(self):
        self.browser.get('https://www.facebook.com/')
        sleep(5)
        self.browser.maximize_window()
        emailInput = self.browser.find_element_by_id("email")
        passwordInput = self.browser.find_element_by_id("pass")
        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        login_box = self.browser.find_element_by_id('u_0_d')
        login_box.click() 
        sleep(5)

    def friendRequestLocation(self):
        self.signIn()
        lnks=self.browser.find_elements_by_tag_name("a")
        for a in self.browser.find_elements_by_xpath('.//a'):
            url = a.get_attribute('href')
            if 'profile.php?id=' in url:
                break
        sleep(5)
        self.browser.get(url)
        sleep(5)
        location = self.browser.find_element(By.XPATH, '//*[@id="mount_0_0"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div[2]/div/div[1]/div[2]/div/div[1]/div/div/div/div/div[2]/div[1]/div/ul/div[5]/div[2]/div/div/span/a/div/span').text
        sleep(5)
        self.browser.get(f"https://www.facebook.com/search/people/?q={str(location)}")
        sleep(5) 
        friendRequest = self.browser.find_element(By.XPATH, '//*[@id="mount_0_0"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div[3]/span/div')
        friendRequest.click()
        sleep(2)

    def updateStatus(self):
        self.signIn()
        lnks=self.browser.find_elements_by_tag_name("a")
        for a in self.browser.find_elements_by_xpath('.//a'):
            url = a.get_attribute('href')
            if 'profile.php?id=' in url:
                break
        self.browser.get(f'{url}&sk=about')
        sleep(2)
        self.browser.get(f'{url}&sk=about_life_events')
        sleep(5)
        status = self.browser.find_element_by_class_name('oygrvhab').click()
        

    def commentTimeline(self): 
        self.signIn()
        self.browser.implicitly_wait(20)
        lnks=self.browser.find_elements_by_tag_name("a")
        for a in self.browser.find_elements_by_xpath('.//a'):
            url = a.get_attribute('href')
            if 'profile.php?id=' in url:
                break
        self.browser.implicitly_wait(10)  
        self.browser.get(url)
        self.browser.implicitly_wait(10)
        self.browser.get(f'{url}&sk=friends')
        self.browser.implicitly_wait(20)
        containers = self.browser.find_elements_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div/div[4]/div/div/div/div/div/div/div/div/div[3]')
        for items in containers:
            friends = list(items.text.split("\n"))
        self.browser.implicitly_wait(20)     
        friend_list = [0, 3, 6, 9, 12, 15]
        random_num = random.choice(friend_list) 
        self.browser.get(f"https://www.facebook.com/search/top?q={friends[random_num]}")
        self.browser.implicitly_wait(20)
        friend = self.browser.find_element_by_xpath('//*[@id="mount_0_0"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div[1]/div[2]/div[1]/div/div/div[2]/div/div[1]/h3/span/span/div/a').click()
        keyboard.press_and_release('j', 'c')
        keyboard.write('nice')
        keyboard.press_and_release('enter')
        sleep(3)
        

bot = FacebookBot('email', 'password')
bot.updateStatus()




