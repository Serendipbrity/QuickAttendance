import pyautogui
import time

# print( pyautogui.size())
# pyautogui.displayMousePosition()
# pyautogui.moveTo(2466,407)
time.sleep(1) 
pyautogui.click()

numberOfStudents = 56

for x in range(numberOfStudents):
    pyautogui.press('down')
    pyautogui.press('tab')  
    pyautogui.press('tab')      


    print('Mouse clicked ' + str(x+1) + ' times')