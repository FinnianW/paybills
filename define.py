billLinks = {}
def programUse(configContent):
    if "billLinks" in configContent:
        return True
    else:
        return False


def newConfiguration():
    numberOfBills = int(input("Welcome, How many bills would you like to setup? "))
    for i in range(numberOfBills):
        key = input("Please enter the name of the #%d bill: "%(i+1))
        value = input("Please enter the full url of the payment portal: ")
        billLinks[key]=value
        print (billLinks)

newConfiguration()
"""
    >>>User input (n)
    Please enter the website followed by the nickname of the n bill (example https://rent.com, rent) 
    >>>User input
    Repeat for n times

    create dictionary with values and their links (ex billLinks={"rent": "https://rent.com", "electric": https://electric.com"... }
    
    save dict to config.txt
def preConfigured
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