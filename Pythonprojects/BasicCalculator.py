# Making a VERY basic calculator as a small project
import sys # for closing program

OpChoice = ""

CanUseProgram = True

# Functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def getinputformath(boolval, answer):
    if boolval == True:
        print("Select a math operation\n")

        print("1 = Add")
        print("2 = Subtract")
        print("3 = Multiply")
        print("4 = Divide")

        opchoice = input("\nEnter a choice here | ")  # Getting input for the operator

        if opchoice in ("1", "2", "3", "4"):
            num1 = ""
            num2 = ""

            while True:
                try:
                    num1 = float(input("\nInput first number | "))  # Making them floats so it can be a number or decimal number
                    num2 = float(input("Input second number | "))
                except ValueError:
                    print("\nNot an integer.")
                    continue
                else:
                    break

            if opchoice == "1":
                print("\n", num1, "+", num2, "=", add(num1, num2))
                ans = add(num1, num2)
                domoremath(ans)

            elif opchoice == "2":
                print("\n", num1, "-", num2, "=", subtract(num1, num2))
                ans = subtract(num1, num2)
                domoremath(ans)

            elif opchoice == "3":
                print("\n", num1, "*", num2, "=", multiply(num1, num2))
                ans = multiply(num1, num2)
                domoremath(ans)

            elif opchoice == "4":
                print("\n", num1, "/", num2, "=", divide(num1, num2))
                ans = divide(num1, num2)
                domoremath(ans)
        else:
            print("\nInvalid choice.\n")
            getinputformath(True, None)
    elif boolval == False:
        print("Select a math operation\n")

        print("1 = Add")
        print("2 = Subtract")
        print("3 = Multiply")
        print("4 = Divide")

        opchoice = input("\nEnter a choice here | ")  # Getting input for the operator

        if opchoice in ("1", "2", "3", "4"):
            num2 = ""

            while True:
                try:
                    num2 = float(input("\nInput a number to add on to " + str(answer) + " | "))
                except ValueError:
                    print("\nNot an integer.")
                    continue
                else:
                    break

            if opchoice == "1":
                print("\n", answer, "+", num2, "=", add(answer, num2))
                ans = add(answer, num2)
                domoremath(ans)

            elif opchoice == "2":
                print("\n", answer, "-", num2, "=", subtract(answer, num2))
                ans = subtract(answer, num2)
                domoremath(ans)

            elif opchoice == "3":
                print("\n", answer, "*", num2, "=", multiply(answer, num2))
                ans = multiply(answer, num2)
                domoremath(ans)

            elif opchoice == "4":
                print("\n", answer, "/", num2, "=", divide(answer, num2))
                ans = divide(answer, num2)
                domoremath(ans)
        else:
            print("\nInvalid choice.\n")
            getinputformath(False, answer)

def domoremath(answer):
    yesno = input("\nDo you want to do anything else, type conton to contiune onto current answer (y/n/conton) | ")

    yesno.lower()

    if yesno in ("y", "n", "conton"):
        if yesno == "y":
            print("\n")
            getinputformath(True, None)
        elif yesno == "n":
            print("\nExiting program")
            sys.exit(None)
        elif yesno == "conton":
            getinputformath(False, answer)
    else:
        print("\nInvalid input")
        domoremath(answer)

if CanUseProgram:
    getinputformath(True, None)
else:
    print("Program not active...")
