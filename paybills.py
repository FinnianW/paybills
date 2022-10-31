#pseudo code 
#This is a change

"""Pseudo code

Check config.txt for previous configurations.
"""
configContent = ""

with open ("config.txt", "r+") as file:
    configContent = file.read()
    print(configContent)

def programUse(configContent):
    if "billList" in configContent:
        print("programUse True")
        return True
    else:
        print("programUse False")
        return False
"""
If new:
    Welcome user. How many bills do we need to pay?
    >>>User input (n)
    Please enter the website followed by the nickname of the n bill (example https://rent.com, rent) 
    >>>User input
    Repeat for n times

    create dictionary with values and their links (ex billLinks={"rent": "https://rent.com", "electric": https://electric.com"... }
    
    save dict to config.txt

If preconfigured:
    Welcome user. What bills are we paying today?
    list keys from billLinks and option to add, delete, or change a key and value (sort alphabetical?)

#Open value webpage where a is the key from billLinks
def openBill(a)
    open billLinks{a} #get value of key a

#Create a new key:value pair
def addBill()
    a = user input 
    b = user input 
    append billLinks("a":"b") 

#Delete a key:value pair
def removeBill()
    a = user input
    del billLinks["a"]


def saveConf(billLinks)
    overwrite billLinks as billLinks in config file

def closeProgram(f):
    #close config.txt
    f.close()
"""
programUse(configContent)
