#pseudo code 
#This is a change

"""Pseudo code

Check config.txt for previous configurations.
"""
import webbrowser
from define import *
configContent = ""

with open ("config.txt", "r+") as file:
    configContent = file.read()
    print(configContent)

programUse(configContent)

if programUse(configContent):
    print ("used")
    #preConfigured()
else:
    print("new")
    #newConfiguration()

webbrowser.open('https://google.com') 

