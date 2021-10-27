print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

print("Treasure only comes to curious people!")
print("Take part in the adventure to gain curiosity points!")
curiousity = 0
print("\n")
print("You've reached the leap year frog.")
print("Type [ask] to see the frog's leap year skills.")

frog_question = input("Type [kick] to wave the frog goodbye. ")

if frog_question.lower() == "ask":
  year = int(input("Which year do you want to check for leap year?: "))
  isLeap = False
  if (year / 4) % 1 == 0.0:
    isLeap = True
    if ((year / 100) % 1) == 0.0:
      isLeap = False
    if ((year / 400) % 1) == 0.0:
      isLeap = True
  else:
    isLeap = False

  if isLeap == True:
    print(f"{year} is leap year.")
  else:
    print(f"{year} is not leap year.")
  
  print("The frog showed you her leap year skills and you move on.")
  curiousity += 1

else:
  print("\n")
  print("Guess you weren't curious enough! Moving on...")

print("\n")
print("You've reached Franco's Island Pizzeria.")
print("Write [hungry] to see Franco's specials.")
pizza_question = input("Write [slime] if you don't like pizza. ")

if pizza_question.lower() == "hungry":
  print("Welcome to Franco's Island Pizzeria!")
  size = input("What size pizza do you want? S, M, or L ")
  add_pepperoni = input("Do you want pepperoni? Y or N ")
  extra_cheese = input("Do you want extra cheese? Y or N ")

  bill = 0

  if size == "S":
    bill = 15
  elif size == "M":
    bill = 20
  elif size == "L":
    bill = 25
  else:
    print("Unrecognized size")
    print("You're getting a large")
    bill = 25

  if add_pepperoni == "Y":
    if size == "S":
      bill += 2
    else:
      bill += 3

  if extra_cheese == "Y":
    bill += 1

  print(f"Your final bill is: ${bill}")
  print("You pay with coconut shells and move on.")
  print("\n")
  curiousity += 1
else:
  print("\n")
  print("Who doesn't like pizza? Weird.")

print("You approach the Island's Turtle Tom the Love Matchmaker!")
print("Write [seek] if you want to hear Tom's wisdom.")
love_question = input("Write [ew] if you are happy alone. ")

if love_question.lower() == "seek":
  print("Welcome to the Love Calculator!")
  name1 = input("What is your name? \n")
  name2 = input("What is their name? \n")

  both_names = (name1 + name2)

  true_count = 0
  love_count = 0

  both_names.lower()

  true_count += both_names.count("t")
  true_count += both_names.count("r")
  true_count += both_names.count("u")
  true_count += both_names.count("e")

  love_count += both_names.count("l")
  love_count += both_names.count("o")
  love_count += both_names.count("v")
  love_count += both_names.count("e")

  love_score = int(str(true_count) + str(love_count))

  if love_score < 10 and love_score > 90:
    print(f"Your love score is {love_score}, you go together like coke and mentos.")
  elif love_score >= 35 and love_score <= 60:
    print(f"Your love score is {love_score}, you are made for eachother.")
  else:
    print(f"Your love score is {love_score}, you're just meh.")

    print("\n")


  curiousity += 1

else:
  print("\n")
  print("Not everyone's gotta have somebody!")

print("You approch the curiousity Wizard and he challenges your curiosity.")
if curiousity >= 2:
  print("The Wizard rewards your curiosity with the Island's Treasure!\n")
else:
  print("You weren't curious enough. Eat sand.\n")

print("THE END")