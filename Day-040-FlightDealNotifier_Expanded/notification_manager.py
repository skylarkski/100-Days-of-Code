import smtplib
import os
import requests
import string
import random

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self) -> None:
        self.mail_sender = os.environ.get('GOOGLE_SMTP_MAIL_SENDER')
        self.mail_receiver = os.environ.get('GOOGLE_SMTP_MAIL_RECEIVER')
        self.password = os.environ.get('GOOGLE_SMTP_AUTH')
        self.TINYURL_AUTH = os.environ.get('TINYURL_AUTH')
        self.TINYURL_ENDPOINT = "https://api.tinyurl.com"

    #Decided not to use as chrome blocks certain proxies that tinyurl uses
    def shorten_url(self, email_to_shorten):

        res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=25))

        query = {
            "url": email_to_shorten,
            "alias": res,
            "api_token": self.TINYURL_AUTH
        }
        
        response = requests.post(url=self.TINYURL_ENDPOINT + "/create", json=query)

        print(response)
        print(response.json())

        small_link = response.json()['data']['tiny_url']

        return small_link

    def send_mail(self, f_dict):

        small_link = f_dict['flight_link']

        email_subject = f"Subject:Cheap flight to {f_dict['arrival_city_name']} found!\n\n"
        email_body = f"We have found a flight to {f_dict['arrival_city_name']} for just ${f_dict['flight_price']}!\nFrom {f_dict['departure_city_name']}-{f_dict['departure_city_code']} to {f_dict['arrival_city_name']}-{f_dict['arrival_city_code']}\nFrom {f_dict['outbound_date']} to {f_dict['inbound_date']}.\n\n"
        email_link = f"Link to flight: {small_link}"
        whole_email = email_subject + email_body + email_link
        
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.mail_sender, password=self.password)
            connection.sendmail(
                from_addr=self.mail_sender, 
                to_addrs=self.mail_receiver,
                msg=whole_email
                )
            
    def send_group_mails(self, f_dict, mail):

        small_link = f_dict['flight_link']

        email_subject = f"Subject:Cheap flight to {f_dict['arrival_city_name']} found!\n\n"
        email_body = f"We have found a flight to {f_dict['arrival_city_name']} for just ${f_dict['flight_price']}!\nFrom {f_dict['departure_city_name']}-{f_dict['departure_city_code']} to {f_dict['arrival_city_name']}-{f_dict['arrival_city_code']}\nFrom {f_dict['outbound_date']} to {f_dict['inbound_date']}.\n\n"
        email_link = f"Link to flight: {small_link}"
        whole_email = email_subject + email_body + email_link
        
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.mail_sender, password=self.password)
            connection.sendmail(
                from_addr=self.mail_sender, 
                to_addrs=mail,
                msg=whole_email
                )