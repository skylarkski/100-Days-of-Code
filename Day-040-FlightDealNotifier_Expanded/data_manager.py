import requests
import os
class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.SHEETY_AUTH = os.environ.get('SHEETY_AUTH')
        self.SHEETY_URL = os.environ.get('SHEETY_FLIGHTS_URL_3')
        self.SHEETY_USERS_URL = os.environ.get('SHEETY_FLIGHTS_URL_USERS')

        self.headers = {
            'Authorization' : self.SHEETY_AUTH
        }
    
    def get_url(self):
        return self.SHEETY_URL

    def get_sheet_data(self):
        response = requests.get(url=self.SHEETY_URL, headers=self.headers)
        return response.json()
    
    def get_sheet_user_data(self):
        response = requests.get(url=self.SHEETY_USERS_URL, headers=self.headers)
        return response.json()
    
    def get_single_row(self, id):
        response = requests.get(url=self.SHEETY_URL + f"/{id}", headers=self.headers)
        return response.json()

    def send_row_data(self, data):
        to_update = {'price': data}
        full_url = self.SHEETY_URL + f"/{to_update['price']['id']}"
        response = requests.put(url=full_url, headers=self.headers, json=to_update)