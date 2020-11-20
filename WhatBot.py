from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
#wait = WebDriverWait(driver, 600)
#_3F6QL _2WovP


#to take user input, uncomment the following lines
#name = input('name ')
#msg = input('msg ')
#count = input('count ')

name = ''  #Contact name
msg = ''   #the message to be sent
count = '' #no. of times the message is to be sent

input('After scanning press any key')

#time.sleep(15)

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box =driver.find_element_by_xpath('//div[@class="_1Plpp"]')

# original msg_box = driver.find_element_by_class_name('_39LWd')

#inp_xpath = '//div[@class="input"][@dir="auto"][@data-tab="1"]'
#input_box = wait.until(EC.element_to_be_clickable((By.XPATH, inp_xpath))) 

for i in range(int(count)):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_35EW6')
    button.click()
