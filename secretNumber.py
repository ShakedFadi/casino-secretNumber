__author__ = 'knedlus'

"""import os
os.system("clear")"""
import os
import random


def main():
    secretNumber = random.randint(1,10)
    tries = 0

    os.system("clear")
    print "Welcome to the 'Secret Number', new game at Ninja Casino!\n" \
          "You have 3 tries to guess our secret number!"


    while True:
        try:
            guess = int(raw_input("\nGuess a number between 1 and 10: "))
            if guess < 1 or guess > 10:
                os.system("clear")
                print "\nYou chose number %i." % guess
                print "Remember, you must input and integer between 1 and 10! Try again!"
            else:
                tries += 1
                print "\nYou chose number %i." % guess
                if guess == secretNumber and tries <= 3:
                    print "Yay! You guessed the right number and have become a proud winner of coding class\n!"
                    break
                elif tries >= 3:
                    print "Sry but all your guesses were wrong! Better luck next time!\n"
                    break
                else:
                    if guess < secretNumber:
                        print "Sry but your guess is wrong! The number you are looking for is higher!\n" \
                              "Try again!\n"
                    elif guess > secretNumber:
                        print "Sry but your guess is wrong! The number you are looking for is lower!\n" \
                              "Try again!\n"
        except ValueError:
            os.system("clear")
            print "Remember, you must input an integer between 1 and 10, not a letter or a word! Try again!"



        #print secretNumber
        #print tries


if __name__ == "__main__":
    main()
