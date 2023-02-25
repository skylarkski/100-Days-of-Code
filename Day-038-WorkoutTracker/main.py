import requests
import datetime
import os

NUTRITIONIX_APP_ID = os.environ.get('NUTRITIONIX_APP_ID')
NUTRITIONIX_API_KEY = os.environ.get('NUTRITIONIX_API_KEY')
SHEETY_AUTH = os.environ.get('SHEETY_AUTH')
SHEETY_URL = os.environ.get('SHEETY_WORKOUTS_URL')

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutri_headers = {
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
    "x-remote-user-id": '1'
}

sheety_header = {
    'Authorization' : SHEETY_AUTH
}

exe_params = {
    'query': input("Tell me which exercises you did: "),
    'gender': 'male',
    'weight_kg': 72,
    'height_cm': 181,
    'age': 24
}

#Using strftime() to format the date
today = datetime.date.today().strftime("%d/%m/%Y")
time = datetime.datetime.now().strftime("%H:%M:%S")

response = requests.post(url=exercise_endpoint, json=exe_params, headers=nutri_headers)
#print(response.text)
# response_sheety = requests.get()

data = response.json()['exercises']

for workout in data:
    to_sheety = { "workout": 
                    {
                    "date": today, 
                    "time": time, 
                    "exercise": workout['name'].capitalize(),
                    "duration": workout['duration_min'],
                    "calories": workout['nf_calories']
                    }
                }
    
    response_sheety = requests.post(url=SHEETY_URL, json=to_sheety, headers=sheety_header)