import pyautogui
import time


pyautogui.FAILSAFE = True


while True:
    
    time.sleep(20)
    print("Moving to the right")
    pyautogui.moveRel(300,0,3, pyautogui.easeInBounce)
    time.sleep(20)
    pyautogui.click()
    time.sleep(15)
    print("Moving up")
    pyautogui.moveRel(0,-300,3, pyautogui.easeInElastic)
    time.sleep(20)
    pyautogui.click()
    time.sleep(15)
    print("Moving to the left")
    pyautogui.moveRel(-300,0,3, pyautogui.easeInBounce)
    time.sleep(20)
    pyautogui.click()
    time.sleep(15)
    print("Moving down")
    pyautogui.moveRel(0,300,3, pyautogui.easeInElastic)
