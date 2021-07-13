import pyautogui

#print(pyautogui.position())


#(x=1183, y=90) #search bar
#(x=1357, y=50) #new tab

pyautogui.click(x=1357, y=50,interval = 1)
pyautogui.click(x=1183, y=90,interval = 1)

pyautogui.typewrite("Hello World!",interval=0.25)
pyautogui.typewrite(["enter"],interval=0.5)

# pyautogui.hotkey("ctrl","a")