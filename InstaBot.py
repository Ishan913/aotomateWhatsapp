from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


class InstaBot:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(2)
        user = driver.find_element_by_xpath('//input[@class="_2hvTZ pexuQ zyHYP"]')
        user.clear()
        user.send_keys(self.username)
        pwd = driver.find_element_by_xpath('//input[@name="password"]')
        pwd.clear()
        pwd.send_keys(self.password)
        pwd.send_keys(Keys.RETURN)
        time.sleep(4)
        driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()

    def message(self,name,msg):
        driver = self.driver
        driver.get("https://www.instagram.com/" + name+"/")
        message_button = driver.find_element_by_xpath('//button[@class="fAR91 sqdOP  L3NKy _4pI4F   _8A5w5    "]')
        message_button.click()
        message_box=driver.find_element_by_xpath('//textarea[@placeholder="Message..."]')
        message_box.send_keys(msg)

    def followers(self,name):
        driver = self.driver
        driver.get("https://www.instagram.com/"+ name+ "/")
        driver.find_element_by_xpath('//a[@href="/{}/followers/"]'.format(name)).click()
        time.sleep(2)
        #for i in range(1,3):
         #   driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
          #  time.sleep(2)

        scroll_box = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')
        last_ht, ht=0,1
        while last_ht != ht:
            follow_buttons = scroll_box.find_elements_by_xpath('//button[@class="sqdOP  L3NKy   y3zKF     "]')
            for i in follow_buttons:
                i.click()

            last_ht=ht
            time.sleep(1)
            ht = driver.execute_script("""
            arguments[0].scrollTo(0, arguments[0].scrollHeight); 
            return arguments[0].scrollHeight;
            """,scroll_box)


    def unfollow(self):
        driver = self.driver
        username = self.username
        driver.get("https://www.instagram.com/"+ username +"/")
        driver.find_element_by_xpath('//a[@href="/{}/following/"]'.format(username)).click()
        last_ht,ht=0,1
        scroll_box=driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/ul/div/li[1]/div/div[3]/button')
        while last_ht != ht:
            following_button=driver.find_elements_by_xpath('/html/body/div[4]/div/div[2]/ul/div/li[1]/div/div[3]')
            for i in following_button:
                i.click()
                driver.find_element_by_xpath("//button[contains(text(), 'Unfollow')]").click()

            last_ht=ht
            ht = driver.execute_script("""
                        arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                        return arguments[0].scrollHeight;
                        """, scroll_box)







#a= input("Enter your id: ")
insta = InstaBot("", "") # enter your user id, password
insta.login()
#insta.unfollow()
insta.followers("") #user id of page to visit
#insta.followers("agemotivation")
#insta.message("agnidevb","te")










