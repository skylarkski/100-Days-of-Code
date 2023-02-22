# API and SMS Rain Notifier
Using the API from:
- https://openweathermap.org/api - My source of weather data

With the combination of using the OpenWeatherMap API data, and Twilio SMS capabilities, I was able to create a notifer app

The Twilio phone number I aquired in a free trial allows for SMS sending via the twilio python package

Using OpenWeatherMap's weather code's which pertain to rain, I am sending an SMS to myself via twilio!

I am hosting the main.py on https://www.pythonanywhere.com/, which runs daily at 8am local to me, letting me know whether I am going to face rain today.

Embrace not using the Weather app on your phone!