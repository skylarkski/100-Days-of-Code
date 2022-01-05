import turtle
import pandas

ALIGNMENT = "center"
FONT = ('Lato', 10, 'bold')

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
inserted_states = []

def insert_state(state, x, y):
    state_to_insert = turtle.Turtle()
    state_to_insert.hideturtle()
    state_to_insert.penup()
    state_to_insert.speed(0)
    state_to_insert.goto(x,y)
    state_to_insert.write(state, align=ALIGNMENT, font=FONT)
    inserted_states.append(state)


# Opening file with pandas
state_data = pandas.read_csv("50_states.csv")

all_states = state_data.state.to_list()

print(all_states)

# print(state_data)

keep_going = True
# Main Loop
while keep_going:
    answer_state = screen.textinput(title=f"{len(inserted_states)}/50 States Correct.", prompt="What's another states' name? Type 'Exit' if you're out of guesses!").title()

    if answer_state == "Exit":
        break

    if answer_state in all_states:
        state_name = state_data[state_data.state == answer_state].state.item()
        state_x = int(state_data[state_data["state"] == answer_state]["x"])
        state_y = int(state_data[state_data["state"] == answer_state]["y"])
        insert_state(state_name, state_x, state_y)

    if len(inserted_states) == 50:
        print("Wow! You got them all! Legend!")
        keep_going = False

# states_to_learn.csv

for state in inserted_states:
    all_states.remove(state)

states_df = pandas.DataFrame(all_states)
states_df.columns = ["State"]

print("List to learn saved to csv")

#getting the csv of guessed states
states_df.to_csv("states_to_learn.csv")
