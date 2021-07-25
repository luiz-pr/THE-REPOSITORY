import pyautogui
import time
import os


# Abrir app
os.startfile('cmd.exe')

# Esperar
time.sleep(2)

# Escrever no app
pyautogui.write('title Luiz')

# Apertar tecla enter
pyautogui.keyDown('enter')

# Soltar a tecla enter
pyautogui.keyUp('enter')

# Esperar
time.sleep(2)


# Escrever no app
pyautogui.write('Python')

# Apertar tecla enter
pyautogui.keyDown('enter')

# Soltar a tecla enter
pyautogui.keyUp('enter')

# Esperar
time.sleep(2)

# Escrever no app
pyautogui.write("print('Hello World!...')")

# Apertar tecla enter
pyautogui.keyDown('enter')

# Soltar a tecla enter
pyautogui.keyUp('enter')

# Esperar
time.sleep(2)

# Escrever no app
pyautogui.write("print('Ola meu nome e Luiz')")

# Apertar tecla enter
pyautogui.keyDown('enter')

# Soltar a tecla enter
pyautogui.keyUp('enter')

# Esperar
time.sleep(2)

# Apertar tecla alt
pyautogui.keyDown('alt')

# Pressionar  a tecla f4
pyautogui.press('f4')

 # Soltar a tecla alt
pyautogui.keyUp('alt')