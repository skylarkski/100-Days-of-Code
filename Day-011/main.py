############### Blackjack Project #####################

############### Blackjack House Rules #################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
from art import logo
import os

#cleaning screen after games
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

#card deck - ace becomes 1 if two are delt at once
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#getting cards
def getCards():
  card_one = cards[random.randint(0, (len(cards)-1))]
  card_two = cards[random.randint(0, (len(cards)-1))]

  hand = [card_one, card_two]
  return hand

#getting the total value of cards
def getCardsTotal(hand):
  total = 0
  for x in range(len(hand)):
    total += hand[x]
  return total

#checking if player got double aces
def doubleAceCheck(hand):
  if getCardsTotal(hand) == 22:
    hand[1] = 1
    return hand
  return hand

def showPlayerCards(hand):
  print(f"Your cards: {hand}, current score: {getCardsTotal(hand)}")

def showPlayerFinalCards(hand):
  print(f"Your final cards: {hand}, final score: {getCardsTotal(hand)}")

def showDealerFirstCard(hand):
  print(f"Dealer's first card: {hand[0]}")

def showDealerCards(hand):
  print(f"Dealer's cards: {hand}, current score: {getCardsTotal(hand)}")

def showDealerFinalCards(hand):
  print(f"Dealer's final cards: {hand}, final score: {getCardsTotal(hand)}")

#adding card to hand
def addCard(hand):
  new_card = cards[random.randint(0, (len(cards)-1))]
  hand.append(new_card)
  return hand

#player getting extra cards
def hitOrPass(hand):

  if getCardsTotal(hand) == 21:
    print(f"You got BLACKJACK!")
    return hand
  
  keepTaking = input("Type 'y' to get an another card, type 'n' to pass: ")

  while keepTaking == "y":

    addCard(hand)

    print(f"\nYou get: {hand[(len(hand)-1)]}\n")
    showPlayerCards(hand)

    if getCardsTotal(hand) < 21:
      keepTaking = input("Type 'y' to get an another card, type 'n' to pass: ")

    elif getCardsTotal(hand) == 21:
      print("BLACKJACK!")
      keepTaking == "n"
      showPlayerFinalCards(hand)
      return hand

    else:
      print("BUST!")
      keepTaking == "n"
      showPlayerFinalCards(hand)
      return hand
  
  print("You Pass")
  showPlayerFinalCards(hand)
  return hand

#dealer getting extra cards
def dealerTurn(hand):
  showDealerCards(hand)

  if getCardsTotal(hand) == 21:
    print(f"Dealer got BLACKJACK!")
    return hand

  while getCardsTotal(hand) < 17:
    addCard(hand)
    print(f"Dealer got: {hand[len(hand)-1]}")
  
  if getCardsTotal(hand) >= 22:
    print("Dealer BUSTED!")
  else:
    print("Dealer Passed")

  showDealerFinalCards(hand)
  return hand

#who won conditionals
def whoWon(handPlayer, handDealer):

  if getCardsTotal(handPlayer) > getCardsTotal(handDealer):

    if getCardsTotal(handPlayer) <= 21 and getCardsTotal(handDealer) > 21:
      print("Dealer busted! You won!")

    elif getCardsTotal(handPlayer) <= 21 and getCardsTotal(handDealer) <= 21:
      print("Your hand is better! You Won!")

    elif getCardsTotal(handPlayer) > 21 and getCardsTotal(handDealer) > 21:
      print("Both busted! It's a Draw!")
    
    elif getCardsTotal(handPlayer) > 21 and getCardsTotal(handDealer) <= 21:
      print("You busted! Dealer Won!")

  elif getCardsTotal(handPlayer) < getCardsTotal(handDealer):

    if getCardsTotal(handPlayer) > 21 and getCardsTotal(handDealer) <= 21:
      print("You went over! Dealer Won!")

    elif getCardsTotal(handPlayer) <= 21 and getCardsTotal(handDealer) <= 21:
      print("Dealer's hand is better! Dealer Won!")

    elif getCardsTotal(handPlayer) > 21 and getCardsTotal(handDealer) > 21:
      print("Both busted! It's a Draw!")

    elif getCardsTotal(handPlayer) <= 21 and getCardsTotal(handDealer) > 21:
      print("Dealer busted! You Won!")

  elif getCardsTotal(handPlayer) == getCardsTotal(handDealer):

    if getCardsTotal(handPlayer) > 21:
      print("Both busted! It's a Draw!")

    elif getCardsTotal(handPlayer) <= 21:
      print("Same hands! It's a Draw!")
  
    
while play == "y":
  print(logo)

  #player getting cards
  playerCards = getCards()

  #checking for double aces
  playerCards = doubleAceCheck(playerCards)
  
  showPlayerCards(playerCards)

  #dealer getting cards and checking for aces
  dealerCards = getCards()
  dealerCards = doubleAceCheck(dealerCards)

  #showing dealer's first card
  showDealerFirstCard(dealerCards)

  #dealing player extra cards
  playerCards = hitOrPass(playerCards)

  #dealing dealer extra cards
  dealerCards = dealerTurn(dealerCards)

  #checking who won
  whoWon(playerCards, dealerCards)

  print("\n")

  play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  cls()
  
#Thanks for playing!