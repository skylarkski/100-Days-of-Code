from art import logo
from art import vs
from game_data import data
from random import randint
import os

#to clear screen
def cls():
    os.system('cls' if os.name=='nt' else 'clear')



def intro():
  print(logo)

def getStars():
  starA = randint(0, len(data)-1)

  starB = starA
  while starA == starB:
    starB = randint(0, len(data)-1)

  starArr = [starA,starB]
  return starArr

def getStats(starA,starB):
  print(f"Compare A: {data[starA]['name']}, a {data[starA]['description']}, from {data[starA]['country']}")
  print(vs)
  print(f"Against B: {data[starB]['name']}, a {data[starB]['description']}, from {data[starB]['country']}")

def getChoice(starA,starB):
  choice = input("Who has more followers? Type 'A' or 'B': ").upper()

  if choice == "A":
    if data[starA]['follower_count'] > data[starB]['follower_count']:
      return True
    else:
      return False
  elif choice == "B":
    if data[starA]['follower_count'] < data[starB]['follower_count']:
      return True
    else:
      return False
  else:
    print("Wrong input")
    return False

def upScore(win, score):
  if win == True:
    score += 1
    return score
  else:
    return score

def showScore(score):
  if win == True:
    print(f"You're right! Current score: {score}")

def resetScore():
  score = 0
  return score
  

score = 0
win = True

while win == True:
    
  cls()
  intro()
  
  if score > 0:
    showScore(score)

  starArr = getStars()
  
  starA = starArr[0]
  starB = starArr[1]

  getStats(starA, starB)

  win = getChoice(starA,starB)

  score = upScore(win, score)

  if win == False:
    print(f"Sorry, that's wrong. Final score: {score}")
    playAgain = input("\nWould you like to play again? (y/n): ")
    if playAgain == "y":
      win = True
      score = 0
    
  

 
