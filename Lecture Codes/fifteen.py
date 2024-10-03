import pyautogui

screenshot = pyautogui.screenshot()
screenshot.save('screenshot.png')

region_screenshot = pyautogui.screenshot(region=(0,0,300,400))
region_screenshot.save('region_screenshot.png')