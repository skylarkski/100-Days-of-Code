import smtplib
import os
class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self) -> None:
        self.mail_sender = os.environ.get('GOOGLE_SMTP_MAIL_SENDER')
        self.mail_receiver = os.environ.get('GOOGLE_SMTP_MAIL_RECEIVER')
        self.password = os.environ.get('GOOGLE_SMTP_AUTH')

    def send_mail(self, f_dict):

        email_subject = f"Subject:Cheap flight to {f_dict['arrival_city_name']} found!\n\n"
        email_body = f"We have found a flight to {f_dict['arrival_city_name']} for just ${f_dict['flight_price']}!\nFrom {f_dict['departure_city_name']}-{f_dict['departure_city_code']} to {f_dict['arrival_city_name']}-{f_dict['arrival_city_code']}\nFrom {f_dict['outbound_date']} to {f_dict['inbound_date']}.\n\n"
        email_link = f"Link to flight: {f_dict['flight_link']}"
        whole_email = email_subject + email_body + email_link

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=self.mail_sender, password=self.password)
            connection.sendmail(
                from_addr=self.mail_sender, 
                to_addrs=self.mail_receiver,
                msg=whole_email
                )