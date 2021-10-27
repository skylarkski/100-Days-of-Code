from art import logo

print(logo)

#calculate function taking both numbers and operator
def calc(first, second, operation):

  if operation == "+":
    return first + second
  elif operation == "-":
    return first - second
  elif operation == "*":
    return first * second
  elif operation == "/":
    return first / second

#getting first number outside of main loop
f_num = float(input("What's the first number?: "))
#result stored as first number for continuing calculation
result = f_num
keepGoing = "y"

print("+\n-\n*\n/")

#main loop
while keepGoing == "y" or keepGoing == "n":

  #get first number again for new calculation
  if keepGoing == "n":
    f_num = float(input("What's the first number?: "))
  else:
    f_num = result

  operation = input("Pick an operation: ")
  #misinput identification
  while operation != "+" and operation != "-" and operation != "*" and operation != "/":
    operation = input("Pick an operation: ")
  
  n_num = float(input("What's the next number?: "))

  #getting result from calc function
  result = calc(f_num,n_num,operation)

  print(f"{f_num} {operation} {n_num} = {result}")

  keepGoing = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation, type 'q' to quit: ")