import pyautogui
import time
from PIL import Image
import pytesseract
import csv



Governors = []

currentNumber = 1
numberOfGovs = 0
# Constants for image location
PROFILE = (83, 92)
RANKINGS = (660, 807)
POWERRANKS = (463, 627)
EXITRANK = (1600, 152)
MOREINFO = (458, 817)
KILLPOINTS = (1313, 443)
EXITMOREINFO = (1635, 98)

# first 5 ranks need to be hard coded in as they dont move positions.
RANK1 = (948, 360)
RANK2 = (948, 480)
RANK3 = (948, 600)
RANK4 = (948, 720)



# the game auto adjusts so no changes are need to be made.
RANK = (948, 720)
# locations where the photos are grabbed
#talk about the problem of getting these locations and how i solved it in powerpoint and in summary of artefact aswell:)

Name = (757, 335, 331, 64)
ID = (904, 302, 115,51)
KP = (1316, 458, 229, 45)
dead = (1383, 534, 174, 66)
rssass = (1352, 807, 204, 61)
t4 = (1481, 866, 188, 44) #this is the points so be sure to /10 to find the number of t4 kills. Same applies for tier 5 but instead /20.
t5 = (1481, 920, 188, 44)
power = (1055, 455, 195, 45)




# Paths for all of the files
DeadPath = r"C:\Users\jackk\__HPQ school project\HPQ-Project\Dead"
IdsPath = r"C:\Users\jackk\__HPQ school project\HPQ-Project\Ids"
KillsPath = r"C:\Users\jackk\__HPQ school project\HPQ-Project\Kill Points"
NamesPath = r"C:\Users\jackk\__HPQ school project\HPQ-Project\Names"
PowerPath = r"C:\Users\jackk\__HPQ school project\HPQ-Project\Power"
T4Path = r"C:\Users\jackk\__HPQ school project\HPQ-Project\T4"
T5Path = r"C:\Users\jackk\__HPQ school project\HPQ-Project\T5"
RssPath = r"C:\Users\jackk\__HPQ school project\HPQ-Project\Rss"

def write_csv(listOfObjs):
    header = ["Name", "ID", "Kills", "Power", "Dead", "T4 KP", "T5 KP", "Rss Assistance"]
    with open('Data.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)

        for obj in listOfObjs:
            data = [obj.name, obj.id, obj.kills, obj.power, obj.deads, obj.t4, obj.t5, obj.rss]
            writer.writerow(data)
    
def scanImage(filename):
    return pytesseract.image_to_string(Image.open(filename))

def grabInfo(location, pathOfType):
    path = (pathOfType + "\ " + str(currentNumber) + ".png")
    image = pyautogui.screenshot(region=location)
    image.save(path)
    time.sleep(2)

    return scanImage(path)

class Governor:
    def __init__(self, deads, id, kills, name, power, t4, t5, rss):
        self.deads = deads
        self.id = id
        self.kills = kills
        self.name = name
        self.power = power
        self.t4 = t4
        self.t5 = t5
        self.rss = rss

def click(pos):
    pyautogui.moveTo(pos)
    time.sleep(1)
    pyautogui.click()

def getPlayerInfo():
    global currentNumber

    print("Getting name from governor " + str(currentNumber) + ": ")
    nameOfGov = grabInfo(Name, NamesPath)
    print("Governor name: " + nameOfGov)

    print("Getting ID from governor " + str(currentNumber) + ": ")
    IDOfGov = grabInfo(ID, IdsPath)
    print("Governor ID: " + IDOfGov)

    print("Getting kill points from governor " + str(currentNumber) + ": ")
    killsOfGov = grabInfo(KP, KillsPath)
    print("Governor kill points: " + killsOfGov)

    print("Getting power from governor " + str(currentNumber) + ": " )
    powerOfGov = grabInfo(power, PowerPath)
    print("Governor power: " + powerOfGov)

    time.sleep(1)
    click(KILLPOINTS)
    time.sleep(3)
    print("Getting t4 kills from governor " + str(currentNumber) + ": ")
    t4kills = grabInfo(t4, T4Path)
    print("Governor t4 kill points: " + t4kills)

    print("Getting t5 kills from governor " + str(currentNumber) + ": ")
    t5kills = grabInfo(t5, T5Path)
    print("Governor t5 kill points: " + t5kills)


    click(MOREINFO)
    time.sleep(2)
    print("Getting deads from governor + " + str(currentNumber) + ": ")
    deads = grabInfo(dead, DeadPath)
    print("Governor deads: " + deads)

    print("Getting resource assistance from governor + " + str(currentNumber) + ": ")
    resourceass = grabInfo(rssass, RssPath)
    print("Governor resource assistance: " + resourceass)

    #adding to an array of objects so it maybe works with excel but probably not.
    gov = Governor(deads, IDOfGov, killsOfGov, nameOfGov, powerOfGov, t4kills, t5kills, resourceass)
    Governors.append(gov)

    currentNumber += 1
    click(EXITMOREINFO) #location to click of the more info screen
    click(EXITRANK)

def mainProc():
    global numberOfGovs

    if numberOfGovs == 1:
        click(RANK1)
        time.sleep(3)
        getPlayerInfo()
        time.sleep(2)
    elif numberOfGovs == 2:
        click(RANK2)
        time.sleep(3)
        getPlayerInfo()
        time.sleep(2)
    elif numberOfGovs == 3:
        click(RANK3)
        time.sleep(3)
        getPlayerInfo()
        time.sleep(2)
    elif numberOfGovs == 4:
        click(RANK4)
        time.sleep(3)
        getPlayerInfo()
        time.sleep(3)
    
    for i in range((numberOfGovs - 4)):
        click(RANK)
        time.sleep(3)
        getPlayerInfo()
        time.sleep(1)

    write_csv(Governors)

def startup():
    global numberOfGovs
    numberOfGovs = int(input("How many governors inforation should i grab?"))
    click(PROFILE)
    click(RANKINGS)
    click(POWERRANKS)
    mainProc()

startup()