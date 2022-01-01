#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".


with open("Input/Names/invited_names.txt") as inv_names_file:
    inv_names = inv_names_file.read().split()
    print(inv_names)

with open("Input/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()

    print(letter)

#for every name in array, replace placeholder with name and save new letter
for name in inv_names:
    new_letter = letter
    to_write = new_letter.replace("[name]", name)

    #opening new file to write modified letter to
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode="w") as letter_to_write:
        letter_to_write.write(to_write)
