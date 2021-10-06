char = ["roadhog","doomfist","hanzo", "widowmaker","zenyatta"]
print(*char, sep = ", ")
print("")

while True:
    choice = input("Choose a character from the choices above: ")
    choice = choice.lower()
    
    while choice in (char):
        if choice == char[0]:
            pickedvar = char[0]
            print("\nPicked: " + pickedvar)

            confirm = input("Are you sure you want to pick " + pickedvar + " (y/n)")
            confrim = confirm.lower()

            if confrim in ("y","n"):
                if confirm == "y":
                    print("\nPicked: \"y\"")
                    print("\nGood choice, you can now again:")
                    break
                elif confirm == "n":
                    print("\nPicked: \"n\"")
                    break
            else:
                print("Invalid answer to input")
                continue
        elif choice == char[1]:
            pickedvar = char[1]
            print("\nPicked: " + pickedvar)

            confirm = input("Are you sure you want to pick " + pickedvar + " (y/n)")
            confrim = confirm.lower()

            if confrim in ("y","n"):
                if confirm == "y":
                    print("\nPicked: \"y\"")
                    print("\nGood choice, you can now again:")
                    break
                elif confirm == "n":
                    print("\nPicked: \"n\"")
                    break
            else:
                print("Invalid answer to input")
                continue

        elif choice == char[2]:
            pickedvar = char[2]
            print("\nPicked: " + pickedvar)

            confirm = input("Are you sure you want to pick " + pickedvar + " (y/n)")
            confrim = confirm.lower()

            if confrim in ("y","n"):
                if confirm == "y":
                    print("\nPicked: \"y\"")
                    print("\nGood choice, you can now again:")
                    break
                elif confirm == "n":
                    print("\nPicked: \"n\"")
                    break
            else:
                print("Invalid answer to input")
                continue

        elif choice == char[3]:
            pickedvar = char[3]
            print("\nPicked: " + pickedvar)

            confirm = input("Are you sure you want to pick " + pickedvar + " (y/n)")
            confrim = confirm.lower()

            if confrim in ("y","n"):
                if confirm == "y":
                    print("\nPicked: \"y\"")
                    print("\nGood choice, you can now again:")
                    break
                elif confirm == "n":
                    print("\nPicked: \"n\"")
                    break
            else:
                print("Invalid answer to input")
                continue

        elif choice == char[4]:
            pickedvar = char[4]
            print("\nPicked: " + pickedvar)

            confirm = input("Are you sure you want to pick " + pickedvar + " (y/n)")
            confrim = confirm.lower()

            if confrim in ("y","n"):
                if confirm == "y":
                    print("\nPicked: \"y\"")
                    print("\nGood choice, you can now again:")
                    break
                elif confirm == "n":
                    print("\nPicked: \"n\"")
                    break
            else:
                print("Invalid answer to input")
                continue
    continue

               
    




