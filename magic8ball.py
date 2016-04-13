# I'm sure you've used a magic 8 ball at one point in your life. You ask it a question, turn it right side up
# and it gives an answer by way of a floating die with responses written on it. You can create one in python. You must:
# Allow the user to enter their question
# Display an in progress message( i.e. "thinking")
# Create 20 responses, and show a random response
# Allow the user to ask another question or quit
# Bonus Using whatever module you like, add a gui. Your gui must have:
# A box for users to enter the question
# At least 4 buttons: Ask , clear(the text box), play again and quit(this must close the window)

import random
import time

eight_ball = [ "It is certain", "It is decidedly so", "Without a doubt", "Yes, definitely",
               "You may rely on it", "As I see it, yes", "Most Likely", "Outlook Good",
               "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later",
               "Better not tell you now", "Cannot predict now", "Concentrate and ask again",
               "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very Doubtful"]

def question():
    question = raw_input("You may ask your yes or no question of the Magic 8 Ball!\n")
    print("Thinking...")
    time.sleep(random.randrange(0,5))
    print(random.choice(eight_ball))

while True:
    question()
    repeat = raw_input("Would you like to ask another question? (Y or N)")
    if not (repeat == "y" or repeat == "Y"):
        print "Come back if you have more questions!"
        break