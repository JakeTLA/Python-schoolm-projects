import time
import sys

X = 2
Y = 4

while True:
    if X != Y:
        print("X and Y values are not equal")
        time.sleep(.5)
        inputvar = input("do you want to continue the loop? (y,n)\n")
        inputvar = inputvar.lower()

        X += 1
        
        while inputvar in ("y","n"):
            if inputvar == "y":
                break
            elif inputvar == "n":
                sys.exit()
        else:
            print("Invalid answer to input")
            X -= 1
            continue
        continue
    elif X >= Y:
        print("X now equal to Y")
        sys.exit()
    else:
        print("error")
        sys.exit()
