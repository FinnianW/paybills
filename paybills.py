#pseudo code 
#This is a change

"""Pseudo code

Check config.txt for previous configurations.
If new:
    Welcome user. How many bills do we need to pay?
    >>>User input (n)
    Please enter the website followed by the nickname of the n bill (example https://rent.com, rent) 
    >>>User input
    Repeat for n times

    create dictionary with values and their links (ex mylinks={"rent": "https://rent.com", "electric": https://electric.com"... }
    
    save dict to config.txt

If preconfigured:
    Welcome user. What bills are we paying today?
    list keys from mylinks and option to add, delete, or change a key and value (sort alphabetical?)

#Open value webpage where a is the key from mylinks
def openBill(a)
    open mylinks{a} #get value of key a

#Create a new key:value pair
def addBill()
    a = user input 
    b = user input 
    append mylinks("a":"b") 

#Delete a key:value pair
def removeBill()
    a = user input
    del mylinks["a"]


def saveConf(mylinks)
    overwrite mylinks as mylinks in config file

def closeProgram()
    close config.txt

    


"""