import pytesseract
import pyautogui
from PIL import Image
location = pyautogui.locateOnScreen("power.png")
print(location)