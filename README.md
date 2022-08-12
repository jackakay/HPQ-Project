
# HPQ Project
![Stat Bot](https://cdn.upload.systems/uploads/BlEy992u.png)
# GUI
Rise of Kingdoms stat bot. Grabs n number of governor information for use for kvk and contributions of governors.
This stat bot has a built-in easy to use GUI. Made in tkinter, its simplistic design helps get things done quickly.
![GUI](https://cdn.upload.systems/uploads/LE4To5kF.png)
# The scan
Once the scan is complete it will let you know through the use of a message box. A terminal will be open as the scan is being complete letting you know of the information being grabbed and how far along your scan is.

A down-side to this stat-bot is that, bluestacks must be open full screen at all times during the scan.
# How to run

Download the repository from my github and make sure these libraries are installed.

    pip install <library>

 - tkinter
 - pyautogui
 - csv
 - pytesseract


You must also download tesseract and add it to your path.
Once all the prerequisites are installed. We can now run the scan.

    python3 main.py
Fill in the required information into the textboxes and hit start. 
# Issues

 - There is an issue with the OCR where the governor ID will sometimes not be seen. I have tried to fix this by grayscaling the image then sharpening it. Tesseract seems to read it much better but keep in mind it can still fail.
 - Also, if a name is in a different alphabet (not English) the OCR will not recognise it and will see it as blank space.

 

 