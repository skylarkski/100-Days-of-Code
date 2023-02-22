import requests
import os
from twilio.rest import Client

#Using my system's enviroment stored variables
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

#Weathermap API
api_key = "YOUR_OPENWEATHERMAP_API_HERE"
OMW_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
bring_umbrella = None

parameters = {
    "q": 'Frisco,US',
    "appid": api_key,
    "cnt": 4
}

response = requests.get(OMW_Endpoint, params=parameters)
response.raise_for_status()

data = response.json()

twelve_hours = data["list"]

for weather_status in twelve_hours:
    for weather_condition in weather_status['weather']:
        if weather_condition['id'] < 700:
            bring_umbrella = True

if bring_umbrella:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☂️",
        from_="YOUR_TWILIO_NUM_HERE",
        to="YOUR_PHONE_NUM_HERE"
    )

    print(message.status)