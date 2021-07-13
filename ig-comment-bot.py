from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import random

DRIVER_PATH = <path of chromedriver> # '/Users/annievan/Downloads/chromedriver'
LOGIN_URL = 'https://www.instagram.com/accounts/login/'
POST_URL = <post_url>
USERNAME = <usrname>
PASSWORD = <pw>
handles = open("handles.txt").read().split('\n') # opens handles.txt and reads all the names

driver = webdriver.Chrome(DRIVER_PATH)
driver.get(LOGIN_URL)

time.sleep(5)

driver.find_element_by_name("username").send_keys(USERNAME)
driver.find_element_by_name("password").send_keys(PASSWORD)

login = driver.find_element_by_class_name("sqdOP.L3NKy.y3zKF") 
login.click()

time.sleep(5)

driver.get(POST_URL)

time.sleep(5)

for name in handles:
    comment = '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea'
    commentArea = driver.find_element_by_xpath(comment)
    commentArea.click()

    time.sleep(5)

    comment = '//*[@id="react-root"]/section/main/div/div[1]/article/div[3]/section[3]/div/form/textarea'
    commentArea = driver.find_element_by_xpath(comment)
    commentArea.send_keys("@" + name)

    post = '//*[@id="react-root"]/section/main/div/div/article/div[3]/section[3]/div/form/button[2]'
    driver.find_element_by_xpath(post).click()

    print(name)
    time.sleep(90)
