import pyautogui
import time
# pyautogui.alert('This is an alert box.')
# pyautogui.confirm('Enter option.', buttons=['A', 'B', 'C'])
print("Now i am writting something for you please wait")
time.sleep(3)
pyautogui.write('I love python', interval=0.25)
pyautogui.press('enter')
