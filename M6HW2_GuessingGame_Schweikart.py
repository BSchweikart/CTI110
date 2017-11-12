# Feet to Inches
# 10/11/2017
# CTI-110 M6HW2_Rndom Number Guessing Game
# Brian Schweikart
#

# Inport the guessing game
import random
guessesTaken = 0

# User inputs name
print("Hello! What is your name?")
myName = input()

# Number range
number = random.randint (1,100)
print("Well, " + myName + ", I want to play a game, I'm thinking of a number between 1 and 100.")

# Total number of guess allowed
while guessesTaken < 10:
	print("Take a guess.")
	guess = input()
	guess = int(guess)
	
	# Adds total number of guesses to count
	guessesTaken = guessesTaken + 1
	
	# If guess is to low or to high along with max count reached or number guessed
	if guess < number:
		print("Your guess is to low.")
		
	if guess > number:
		print("Your guess is to high")
		
	if guess == number:
		break
		
		
if guess == number:
	guessesTaken = str(guessesTaken)
	print("Good job," + myName + "! You guessed my number in " + guessesTaken + " guesses!")
	
if guess != number:
	number = str(number)
	print("I'm sorry the number I was thinking of was " + number)