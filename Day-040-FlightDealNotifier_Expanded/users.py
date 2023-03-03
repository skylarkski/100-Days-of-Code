import os
import requests

sheety_url = os.environ['SHEETY_FLIGHTS_URL_USERS']
sheety_auth = os.environ['SHEETY_AUTH']

header = {
    "Authorization": sheety_auth
}
def get_info():
        
    first_name = input("- What is your first name?\n")
    last_name = input("- What is your last name?\n")

    email_1 = input("- What is your email?\n")
    email_2 = input("- Type your email again.\n")

    while email_1 != email_2:
        email_2 = input("- Email's don't match.\n- Type your email again.\n")

    user_info = {
        "user":
        {
            "firstName":first_name,
            "lastName":last_name,
            "email":email_2,
        }
    }
    return user_info

user_info = get_info()

# response = requests.get(url=sheety_url, headers=header)

response = requests.post(url=sheety_url, headers=header, json=user_info)

if response.status_code == 200:
  print("You're in the club!")
elif response.status_code == 402:
  print("Sheety license expired")
else:
  print("Something went wrong")