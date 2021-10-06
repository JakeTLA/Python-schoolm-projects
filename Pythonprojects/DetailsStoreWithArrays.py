import time

def RequestInput():
    print("Input your details here\n")
    name = input("Name? ")
    age = input("Age? ")
    gender = input("Gender? ")

    ShowInputs(name, age, gender)

def ShowInputs(Name, Age, Gender):
    array.clear()

    array.append("Your name " + str(Name)) # Making sure there strings
    array.append("Your age " + str(Age))
    array.append("Your gender " + str(Gender))

    print("\nYour Details...\n")

    print(*array, sep = "\n") # using sep = "\n" so that it makes a new line after every bit of the array

    print("\n")
    
    AskIfRedo()

def AskIfRedo():
    yn = ""
    caninput = False

    time.sleep(1.5)

    caninput = True

    if caninput:
         print("Do you want to change anything? (y/n)\n")
         
         yn = input("")

         yn.lower()

         if yn == "y":
             print("\n")
             RequestInput()
         elif yn == "n":
             print("\nExiting program...")
         else:
             print("Please type \"y\" or \"n\"!\n")
             AskIfRedo()
    
array = []

name = ""
age = ""
gender = ""

programrunable = True

if programrunable:
    RequestInput()
else:
    print("Program not active...")  
