import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

hands = [rock, paper, scissors]

print("What do you choose?\nType 0 for Rock\nType 1 for Paper\nType 2 for Scissors")

human_choice = int(input())

cpu_choice = random.randint(0,2)

print(cpu_choice)
print("\nYou chose:\n")
print(hands[human_choice])
print("\nComputer chose:\n")

print(hands[cpu_choice])



if human_choice == cpu_choice:
  print("It's a Draw!")
elif human_choice == 0 and cpu_choice == 1:
  print("You Lose!")
elif human_choice == 0 and cpu_choice == 2:
  print("You Win!")
elif human_choice == 1 and cpu_choice == 0:
  print("You Win!")
elif human_choice == 1 and cpu_choice == 2:
  print("You Lose!")
elif human_choice == 2 and cpu_choice == 0:
  print("You Lose!")
elif human_choice == 2 and cpu_choice == 1:
  print("You Win!")
