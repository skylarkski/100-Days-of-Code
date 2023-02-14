##################### Birthday Wisher ######################

#Modify the ExtraHard
import datetime as dt
import random
import smtplib
import pandas as pd

#used emails
#ENTER YOUR GMAIL HERE
g_mail = "YOURGMAILHERE"

#gmail app password
#ENTER YOUR GMAIL APP 16 CHARACTER PASSWORD HERE
#Gmail account > Security > Enable 2FA > App passwords > Generate 16 Character Password
password = "YOUR16CHARACTERPASSWORDHERE"

now = dt.datetime.now()
current_day = now.day
current_month = now.month

#getting birthday data from csv
data = pd.read_csv("birthdays/birthdays.csv")
birthday_list = data.to_dict("records")

#finding who has a birthday today
birthday_celebrants = [(person['name'], person['email']) for person in birthday_list if person['month'] == current_month and person['day'] == current_day]

#saving letters
with open("letter_templates/letter_1.txt", "r") as l1:
    letter_1 = l1.readlines()
    
with open("letter_templates/letter_2.txt", "r") as l2:
    letter_2 = l2.readlines()

with open("letter_templates/letter_3.txt", "r") as l3:
    letter_3 = l3.readlines()

#letters list
letters = [letter_1, letter_2, letter_3]

#choosing from the list of celebrants
for celebrant in birthday_celebrants:

    letter_to_celebrant = random.choice(letters)
    #replacing placeholder with celebrant name
    letter_to_celebrant[0] = letter_to_celebrant[0].replace("[NAME]", celebrant[0])

    email_subject = "Subject:Happy Birthday!\n\n"
    email_body = "".join(letter_to_celebrant)
    whole_email = email_subject + email_body

    #sending the email
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=g_mail, password=password)
        connection.sendmail(
            from_addr=g_mail, 
            to_addrs=celebrant[1],
            msg=whole_email
            )