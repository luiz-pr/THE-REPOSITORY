import qrcode
import pyautogui
import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')

class web():
    driver.get('https://web.whatsapp.com/')


time.sleep(15)

class enviar():
    img = qrcode.make('https://luiz-pr.000webhostapp.com/')
    print(type(img))
    print(img.size)
    img.save('qrcode_web.png')

    time.sleep(6)

    driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/div/div[2]').click()

    pyautogui.write('+55 21 97939-4346')
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    
    time.sleep(6)

    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/div').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[1]/div[2]/div/span/div[1]/div/ul/li[3]/button').click()

    time.sleep(6)

    pyautogui.write("C:\qrCode_to_whattsApp\qrcode_web.png")
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')
    time.sleep(6)

    driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div[2]/div[2]/span/div[1]/span/div[1]/div/div[2]/span/div').click()
    
    time.sleep(6)

    print('Enviado com Sucesso')
    time.sleep(6)

driver.quit()