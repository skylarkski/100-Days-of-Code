from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

moreBids = "yes"
top_bid = 0
top_bidder = ""
bidders = {}
print(logo)
print("Welcome to the secret auction program.")


while moreBids == "yes":
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))

  bidders[name] = bid

  moreBids = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  
  if moreBids == "yes":
    clear()

for key in bidders:
  if bidders[key] > top_bid:
    top_bid = bidders[key]
    top_bidder = key

print(f"The winner is {top_bidder} with a bid of ${top_bid}.")

print(bidders)