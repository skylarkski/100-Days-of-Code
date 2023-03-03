import os
import requests
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self.TEQUILA_URL = "https://api.tequila.kiwi.com/locations/query"
        self.TEQUILA_API_KEY = os.environ.get('TEQUILA_AUTH')

    def get_iata_code(self, city):

        self.header = {
            'apikey': self.TEQUILA_API_KEY,
            'Content-Encoding': 'gzip'
        }
        self.parameters = {
            'term': city,
            'location_types' : 'airport',
            'limit': 1
        }

        response = requests.get(url=self.TEQUILA_URL, headers=self.header, params=self.parameters)
        data = response.json()
        iata_code = data['locations'][0]['id']
        return iata_code