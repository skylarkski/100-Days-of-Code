#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

print("Welcome to the tip calculator.")

totalAmt = round(float(input("What was the total bill?: ")), 2)

tipPercent = float(input("What percentage tip would you like to give? 12, 15 or 20? \n"))

partySize = int(input("How many people in your party?: \n"))

payPerPerson = round(((totalAmt * (1 + (tipPercent/100)))/partySize),2)

print(f"Each person should pay: ${payPerPerson}")