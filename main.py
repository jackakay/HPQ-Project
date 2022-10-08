from asyncore import write
from django.forms import ImageField
import pyautogui
import time
from PIL import Image, ImageFilter
import pytesseract
import csv
from discord_hooks import Webhook
import tkinter
import os
import atexit
import threading

Aborted = False
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

directory = os.getcwd()

# Paths for all of the files
DeadPath = r"\Dead"
IdsPath = r"\Ids"
KillsPath = r"\Kill Points"
NamesPath = r"\Names"
PowerPath = r"\Power"
T4Path = r"\T4"
T5Path = r"\T5"
RssPath = r"\Rss"

def write_csv(listOfObjs):
    header = ["Name", "ID", "Kills", "Power", "Dead", "T4 KP", "T5 KP", "Rss Assistance"]
    with open('Data.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(header)

        for obj in listOfObjs:
            data = infoFromObject(obj)
            writer.writerow(data)

def infoFromObject(obj):
    return [obj.name, obj.id, obj.kills, obj.power, obj.deads, obj.t4, obj.t5, obj.rss]

def scanImage(filename):
    return pytesseract.image_to_string(Image.open(filename))

def grabInfo(location, pathOfType):
    path = (str(directory) + pathOfType + "\ " + str(currentNumber) + ".png")
    image = pyautogui.screenshot(region=location)
    image.save(path)
    
    img = Image.open(path).convert("L").filter(ImageFilter.SHARPEN)
    img.save(path)
    time.sleep(1)
    
    info = scanImage(path)
    if pathOfType == IdsPath:
        if not any(char.isdigit() for char in info):
            info = scanImage(path)
            print("First test")
            if not any(char.isdigit() for char in info):
                info = scanImage(path)
                print("Second test")

    return info

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
    #come back to this and add threading.
    nameThread = threading.Thread(target=lambda: )
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
    time.sleep(2)
    print("Getting t4 kills from governor " + str(currentNumber) + ": ")
    t4kills = grabInfo(t4, T4Path)
    print("Governor t4 kill points: " + t4kills)

    print("Getting t5 kills from governor " + str(currentNumber) + ": ")
    t5kills = grabInfo(t5, T5Path)
    print("Governor t5 kill points: " + t5kills)

    click(MOREINFO)
    time.sleep(1.5)
    print("Getting deads from governor + " + str(currentNumber) + ": ")
    deads = grabInfo(dead, DeadPath)
    print("Governor deads: " + deads)

    print("Getting resource assistance from governor " + str(currentNumber) + ": ")
    resourceass = grabInfo(rssass, RssPath)
    print("Governor resource assistance: " + resourceass)

    #adding to an array of objects so it maybe works with excel but probably not.
    gov = Governor(deads, IDOfGov, killsOfGov, nameOfGov, powerOfGov, t4kills, t5kills, resourceass)
    Governors.append(gov)

    currentNumber += 1
    click(EXITMOREINFO) #location to click of the more info screen
    time.sleep(1)
    click(EXITRANK)

def mainProc(kingdom, govs):
    
    webhook_url = "https://discord.com/"
    embed = Webhook(webhook_url, color=123123)
    embed.set_desc("User started scan for kingdom " + kingdom + " and is scanning " + str(govs) + "governors.")
    embed.post()
    if govs < 5:
#doesnt actually work for getting the governors
        if govs == 1:
            click(RANK1)
            time.sleep(1.5)
            getPlayerInfo()
            time.sleep(1.5)
        elif govs == 2:
            click(RANK2)
            time.sleep(1.5)
            getPlayerInfo()
            time.sleep(1.5)
        elif govs == 3:
            click(RANK3)
            time.sleep(1.5)
            getPlayerInfo()
            time.sleep(1.5)
        elif govs == 4:
            click(RANK4)
            time.sleep(1.5)
            getPlayerInfo()
            time.sleep(1.5)
    else:
        click(RANK1)
        time.sleep(1.5)
        getPlayerInfo()
        time.sleep(1.5)

        click(RANK2)
        time.sleep(1.5)
        getPlayerInfo()
        time.sleep(1.5)

        click(RANK3)
        time.sleep(1.5)
        getPlayerInfo()
        time.sleep(1.5)
        
        click(RANK4)
        time.sleep(1.5)
        getPlayerInfo()
        time.sleep(1.5)
        while not Aborted:
            for i in range((govs - 4)):
                if not Aborted:
                    click(RANK)
                    time.sleep(1.5)
                    getPlayerInfo()
                    time.sleep(1.5)
    
    end_embed = Webhook(webhook_url, color=123123)
    end_embed.set_desc("User finished scan for kingdom " + kingdom + " and scanned " + str(govs) + "governors.")
    
    end_embed.post()
    

    write_csv(Governors) 

def startup(window, kingdom, numberOfGovs):
    atexit.register(lambda : write_csv(Governors))
    if kingdom == None and numberOfGovs == None:
        print("Error")
    else:
        print("STARTING BOT")
        click(PROFILE)
        time.sleep(1.5)
        click(RANKINGS)
        time.sleep(1.5)
        click(POWERRANKS)
        time.sleep(1.5)
        mainProc(kingdom, numberOfGovs)
        print("Scan Complete","Your scan is complete, check 'Data.csv' for the information grabbed ")

"""
kingdomnum = input("Kingodom Number: ")
numberOfGovs = int(input("How many governors inforation should i grab?"))
startup(kingdomnum, numberOfGovs)
"""
