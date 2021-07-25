import time
from selenium import webdriver
import pyautogui

driver = webdriver.Chrome(executable_path=r'./chromedriver.exe') 
driver.get('https://www.instagram.com/')

time.sleep(6)

driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div').click()

time.sleep(3)

pyautogui.write('luizzhenriquematias29@gmail.com')

time.sleep(3)

driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div').click()

time.sleep(3)

pyautogui.write('12345678oi')

time.sleep(3)

pyautogui.keyDown('enter')
pyautogui.keyUp('enter')

time.sleep(10)

driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div').click()

time.sleep(3)

driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()

time.sleep(4)

driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/span/img').click()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[2]/div').click()

time.sleep(3)

driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]/a/div/div[2]').click()

time.sleep(3)

driver.find_element_by_xpath('/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea').click()

pyautogui.write('Eu')

pyautogui.keyDown('enter')
pyautogui.keyUp('enter')

# driver.quit()