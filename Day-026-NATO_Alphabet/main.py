import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

nato_dict = {row.letter:row.code for (index, row) in nato_data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Enter a word: ")

nato_list = [nato_dict[i] for i in list(user_input.upper())]

print(nato_list)

