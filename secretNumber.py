__author__ = 'knedlus'

"""import os
os.system("clear")"""
import os
import random


def main():
    secretNumber = random.randint(1,10)
    #print secretNumber
    os.system("clear")
    print "Welcome to the 'Secret Number', new game at Ninja Casino!\n"


    while True:
        try:
            guess = int(raw_input("\nGuess a number between 1 and 10: "))
            if guess < 1 or guess > 10:
                os.system("clear")
                print "\nYou chose number %i." % guess
                print "Remember, you must input and integer between 1 and 10! Try again!"
            else:
                print "\nYou chose number %i." % guess
                break

        except ValueError:
            os.system("clear")
            print "Remember, you must input an integer between 1 and 10, not a letter or a word! Try again!"


    if guess == secretNumber:
        print "Yay! You guessed the right number and have become a proud winner of coding class\n!"
    else:
        print "Sry but your guess is wrong! Better luck next time!\n"


if __name__ == "__main__":
    main()