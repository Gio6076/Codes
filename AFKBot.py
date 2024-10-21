import pyautogui as pag
import random
import time
import keyboard
print("Press N to Exit")

while True:
    if keyboard.is_pressed('n'):
        print("Exiting the program...")
        break
    x = random.randint(600, 700)
    y = random.randint(200, 600)
    pag.moveTo(x,y, 0.5)
    time.sleep(15)
