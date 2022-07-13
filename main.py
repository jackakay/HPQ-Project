import pyautogui
import time
from PIL import Image
import pytesseract

currentNumber = 0

# Constants for image location
PROFILE = (83, 92)
RANKINGS = (660, 807)
POWERRANKS = (463, 627)

# first 5 ranks need to be hard coded in as they dont move positions.
RANK1 = (948, 360)
RANK2 = (948, 480)
RANK3 = (948, 600)
RANK4 = (948, 720)

# the game auto adjusts so no changes are need to be made.
RANK = (948, 720)
# locations where the photos are grabbed
name = (2653, 338, 351, 65)
ID = (2829, 308, 108, 36)
KP = (3242, 455, 245, 42)

# Paths for all of the files
DeadPath = r"C:\Users\jackk\__HPQ school project\Dead"
IdsPath = r"C:\Users\jackk\__HPQ school project\Ids"
KillsPath = r"C:\Users\jackk\__HPQ school project\Kill Points"
NamesPath = r"C:\Users\jackk\__HPQ school project\Names"
PowerPath = r"C:\Users\jackk\__HPQ school project\Power"
T4Path = r"C:\Users\jackk\__HPQ school project\T4"
T5Path = r"C:\Users\jackk\__HPQ school project\T5"


class Governor:
    def __init__(self, deads, id, kills, name, power, t4, t5):
        self.deads = deads
        self.id = id
        self.kills = kills
        self.name = name
        self.power = power
        self.t4 = t4
        self.t5 = t5


def getPlayerInfo():
    print("Getting name from governor " + str(currentNumber) + ": ")
    nameOfGov = grabInfo(name, NamesPath)
    print("Governor name: " + nameOfGov)
    print("Getting ID from governor " + str(currentNumber) + ": ")
    IDOfGov = grabInfo(ID, IdsPath)
    print("Governor ID: ")


def mainProc():
    click(RANK1)
    getPlayerInfo()


def grabInfo(location, pathOfType):
    path = pathOfType + ": " + str(currentNumber) + ".png"
    image = pyautogui.screenshot(path, region=location)
    time.sleep(2)

    return scanImage(path)


def scanImage(filename):
    return pytesseract.image_to_string(Image.open(filename))


def click(pos):
    pyautogui.moveTo(pos)
    time.sleep(3)
    pyautogui.click()


def startup():
    click(PROFILE)
    click(RANKINGS)
    click(POWERRANKS)


# Press the green button in the gutter to run the script.
startup()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/