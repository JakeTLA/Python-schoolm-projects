import random
import time

def main():
    print('Welcome to the number guess game.')
    time.sleep(1)
    print('Enter a number between 1-100. You have 5 chances to guess correctly!')
    time.sleep(1.5)

lives = 5
while lives == 5:
    try:
        num = int(input('Please enter a number: '))
        rNum = random.randrange(1,100)
    except ValueError:
        print("Please enter a number between 1-100."):
        continue
else:
    break

    while num == rNum:
        print('Not a match - sorry!')
        lives += 1
        print ('Lives remaining: ', lives)
        if lives == 0:
            print ('GAME OVER :(')
            print ('The answer was: ', rNum)
            break
        else:
            try:
                if num > rNum:
                    print('Your number is too high!')
                    continue
                else:
                    print('Your number is too low!')
                    continue
            except ValueError:
                print('Please enter a number between 1-100.')
                continue
            else:
               break

    if num == RNum:
        print('YOU WIN!')

    while True:
        again = input('Would you like to play again? (Y/N)').upper()
        if again not in ('y', 'n'):
            print('Invalid input - try again.')
            continue
        elif again == Y:
            main()
        else:
            quit()
            

main()





