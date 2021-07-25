# l2445493@gmail.com

import time
from selenium import webdriver
import pyautogui

driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
driver.get('https://accounts.google.com/AddSession/identifier?hl=en&continue=https%3A%2F%2Fwww.google.com%3Fhl%3Den-US&ec=GAlA8wE&flowName=GlifWebSignIn&flowEntry=AddSession')

time.sleep(4)

driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[1]/div/button').click()

time.sleep(4)

driver.find_element_by_xpath('//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div/ul/li[1]').click()

