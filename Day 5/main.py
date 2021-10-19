#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

passw = []
randpass = []
rng = 0
password = ""
randomized_password = ""

for x in range(0, nr_letters):
  
  rng = random.randint(0, len(letters)-1)
  passw += letters[rng]

for x in range(0, nr_symbols):
  
  rng = random.randint(0, len(numbers)-1)
  passw += numbers[rng]
  
for x in range(0, nr_numbers):
  
  rng = random.randint(0, len(symbols)-1)
  passw += symbols[rng]


#print(passw)
for x in passw:
  password += x

passlen = len(passw)

#randomizing the password by popping from passw array
#we stay in range with the rng as randint range changes as passw gets shorter
for x in range(0, passlen):
  rng = random.randint(0, (len(passw)-1))

  randpass += passw.pop(rng)


for x in randpass:
  randomized_password += x

print(f"\nPassword pre-randomization: {password}\n")
print(f"Password post-randomization: {randomized_password}\n")
