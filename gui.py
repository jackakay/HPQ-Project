from cProfile import label
from msilib import datasizemask
from tkinter import *
from tkinter.ttk import Notebook, Style
import time
import os
import sys
import os.path
import platform
import hashlib
from pyparsing import col


from keyauth import api

loggedIn = False

def getchecksum():
	path = os.path.basename(__file__)
	if not os.path.exists(path):
		path = path[:-2] + "exe"
	md5_hash = hashlib.md5()
	a_file = open(path,"rb")
	content = a_file.read()
	md5_hash.update(content)
	digest = md5_hash.hexdigest()
	return digest


keyauthapp = api(
name = "RoK Stat Bot",
ownerid = "wHLQ5y3bJv",
secret = "cb587c247f898880bc6facf4827fbb7b26222a91977778436e17bbac5126fc15",
version = "1.0",
hash_to_check = getchecksum()
)


def insert():
    print("start")

def loginacc(license_, window):
    
    if keyauthapp.license(license_):
        
        draw_window(window)


def login_window():
    login = Tk()
    login.geometry("350x200")
    login.configure(bg="#383838")

    mainLabel = Label(login, text="Login", font=("Arial", 25))
    mainLabel.config(bg="#383838")
    mainLabel.config(fg="white")
    mainLabel.grid(row=2,column=1)



    tokenLabel = Label(login, text="Token: ", font=("Arial", 14))
    tokenLabel.config(bg="#383838")
    tokenLabel.config(fg="white")
    tokenLabel.grid(row = 4, column = 0)

    token = Entry(login)
    token.configure(bg="#717070", fg="white", width=25)
    token.grid(row=4, column=1)
    button = Button(login, text="press", command= lambda: loginacc(str(token.get()), login), width=25, bg="#717070",activebackground="#EA3715").grid(pady= 10, row=6, column=1)
    login.mainloop()

def draw_window(window):
    
   # #717070
    
    master = Toplevel(window)
    
    window.withdraw()
    master.title("Rise of Kingdoms Stat Bot")
    master.geometry("375x400")
    master.configure(bg="#383838")


    
    mainTitle = Label(master, text="RoK Stat Bot", font=("Arial", 25))
    mainTitle.config(bg="#383838")
    mainTitle.config(fg="white")
    mainTitle.grid(column=1, row=4)
    
    
    kingdomLabel = Label(master, text="Kingdom #: ", font=("Arial", 14))
    kingdomLabel.config(bg="#383838")
    kingdomLabel.config(fg="white")
    kingdomLabel.grid(column=0, row=5)

    kingdom = Entry(master)
    kingdom.configure(bg="#717070", fg="white")
    kingdom.grid(row=5, column=1)

    governorsLabel = Label(master, text="Governors: ", font=("Arial", 14))
    governorsLabel.config(bg="#383838")
    governorsLabel.config(fg="white")
    governorsLabel.grid(column=0, row=7)


    governors = Entry(master)
    governors.configure(bg="#717070", fg="white")
    governors.grid(row=7, column=1)

    startButton = Button(master, bg= "#5EA04A", text="Start", width=15, activebackground="#4DC829",command= insert)
    startButton.grid(row=9, column=1)

    abortButton = Button(master, bg= "#8E3E2F", text="Abort", width=15, activebackground="#EA3715")
    abortButton.grid(row=10, column=1,pady=5)

    #2B2B2B

    infoLabel = Label(text="Info to be grabbed: ", font=("Arial", 11))
    infoLabel.config(bg="#383838")
    infoLabel.config(fg="white")
    infoLabel.grid(column=1, row=11)


    listOfInfo = Listbox(master, height=7, bg = "#2B2B2B", activestyle="dotbox", font="Arial", fg="white")
    
    listOfInfo.insert(1, "• Governor name")
    listOfInfo.insert(2, "• Governor ID")
    listOfInfo.insert(3, "• Power")
    listOfInfo.insert(4, "• Kill points")
    listOfInfo.insert(5, "• T4/T5 Kill points")
    listOfInfo.insert(6, "• Dead troops")
    listOfInfo.insert(7, "• Resource assistance")

    listOfInfo.grid(row=12, column=1)
    master.mainloop()

   
login_window()

