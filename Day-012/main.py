#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random

print(logo)

def intro():
  print("Welcome to Higher / Lower!")


def getDifficulty():
  print("Choose your difficulty (type 1 or 2) :")
  print("1. Easy")
  print("2. Hard")
  diff = input()

  if diff == "1":
    print("You've chosen Easy")
    return 10
  else:
    print("You've chosen Hard")
    return 5

def getNumber():
  num = random.randint(1,100)
  return num

def attemptsRemaining(attempts):
  print(f"You have {attempts} attempts remaining to guess the number.")
  
def getGuess():
  guess = int(input("Make a guess: "))

  return guess

def finishAndPlayAgain(hit, num):
  if hit == False:
    print(f"You've run out of attempts! The answer was {num}")
  
  playAgain = input("Do you want to play again? (y/n)")
  if playAgain == "y":
    return True
  else:
    return False

def gameLoop():

  attempts = getDifficulty()
  hit = False
  num = getNumber()

  while hit == False and attempts > 0:

    attemptsRemaining(attempts)
    guess = getGuess()
    if num == guess:
      print(f"You got it! The answer was {num}")
      hit = True
    elif num > guess:
      print("Too low.")
      attempts -= 1
    elif num < guess:
      print("Too high.")
      attempts -= 1

  if finishAndPlayAgain(hit, num) == True:
    gameLoop()


intro()
gameLoop()