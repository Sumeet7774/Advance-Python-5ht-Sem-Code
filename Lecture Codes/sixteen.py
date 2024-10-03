import pyautogui

location = pyautogui.locateOnScreen('screenshot.png')

if location:
    print(f"Image found at: {location}")
    pyautogui.moveTo(location.left + location.width/2, location.top+location.height/2)
else:
    print("Image not found")
    
if location:
    pyautogui.click(location)