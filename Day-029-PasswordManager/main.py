from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

FONT_NAME = "Lato"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def gen_password():

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():

    f = open("data.txt", "a")

    web = website_entry.get()
    ema = email_user_entry.get()
    pas = password_entry.get()

    data_output =  web + " | " + ema + " | " + pas + "\n"

    if len(web) == 0 or len(pas) == 0:
        messagebox.showinfo(title="Whoopsie daisy", message="Please fill out all fields")
    else:
        is_ok = messagebox.askokcancel(title="Title", message=f"These are the details entered:\nEmail: {ema} "
                                                  f"\nPassword: {pas} \nIs it ok to save?")

        if is_ok:
            f.write(data_output)
            f.close()
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=30, pady=30)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=lock_img)
canvas.grid(column=1, row=0)

#Labels
website_label = Label(text="Website:", font=(FONT_NAME))
website_label.grid(column=0, row=1)

email_user_label = Label(text="Email/Username:", font=(FONT_NAME))
email_user_label.grid(column=0, row=2)

password_label = Label(text="Password:", font=(FONT_NAME))
password_label.grid(column=0, row=3)

#Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()

email_user_entry = Entry(width=35)
email_user_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_user_entry.insert(0, "oskar@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky="EW")

#Buttons
gen_password_button = Button(text="Generate Password", command=gen_password, font=(FONT_NAME,10))
gen_password_button.grid(column=2, row=3)

add_password_button = Button(width=35, text="Add", command=add_password, font=(FONT_NAME, 10))
add_password_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
