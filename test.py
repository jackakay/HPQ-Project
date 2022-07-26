import pytesseract
import pyautogui
from PIL import Image
location = pyautogui.locateOnScreen("power.png")
image = pyautogui.screenshot(region=(1481, 866, 188, 44))
image.save("test.png")
print(location)