import requests
from datetime import datetime, timezone
import smtplib
from time import sleep

#ENTER YOUR LAT AND LONG HERE
MY_LAT = 0 # My latitude
MY_LONG = 0 # My longitude
DEGREE_MARGIN = 5

#used emails
#ENTER YOUR GMAIL HERE
sender_email = "YOURGMAILHERE"
recipient_email = "RECIPIENTEMAILHERE"
#ENTER YOUR GMAIL APP 16 CHARACTER PASSWORD HERE
#Gmail account > Security > Enable 2FA > App passwords > Generate 16 Character Password
password = "YOURPASSWORDHERE"

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

def is_nighttime():
        
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    #Using UTC time with timezone.utc to simplify the conversion of UTC sunrise and sunset data from api.sunrise-sunset.org
    time_now = int(str(datetime.now(timezone.utc)).split(" ")[1][0:2])

    if time_now < sunrise and time_now > sunset:
        return True

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - DEGREE_MARGIN < iss_latitude < MY_LAT + DEGREE_MARGIN and MY_LONG - DEGREE_MARGIN < iss_longitude < MY_LONG + DEGREE_MARGIN:
        return True

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.

if is_nighttime() and is_iss_overhead():
    email_subject = "Subject:The ISS Is Above You!\n\n"
    email_body = "Look up!"
    whole_email = email_subject + email_body

    #sending the email
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=password)
        connection.sendmail(
            from_addr=sender_email, 
            to_addrs=recipient_email,
            msg=whole_email
            )
    #Run every minute till either condition is False
    sleep(60)
