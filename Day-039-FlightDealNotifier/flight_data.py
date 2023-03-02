import os
from time import strftime
import requests
import datetime

class FlightData:
    #This class is responsible for structuring the flight data.
    
    def __init__(self) -> None:
        self.flight_search_endpoint = "https://api.tequila.kiwi.com/v2/search"
        self.TEQUILA_API_KEY = os.environ.get('TEQUILA_SEARCH_AUTH')

        self.header = {
            'apikey': self.TEQUILA_API_KEY,
            'Content-Encoding': 'gzip'
        }

    def find_deal(self, iata_code):

        MY_ORGIN_CODE = 'DFW'
        MY_ORGIN_CITY = 'Dallas'

        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        half_a_year_later = tomorrow + datetime.timedelta(days=180)

        self.parameters = {
            'fly_from': f"airport:{MY_ORGIN_CODE}",
            'fly_to': f"airport:{iata_code}",
            'location_types': 'airport',
            'date_from': tomorrow.strftime("%d/%m/%Y"),
            'date_to': half_a_year_later.strftime("%d/%m/%Y"),
            'flight_type': 'round',
            'curr': 'USD',
            'sort': 'price',
            'limit': '1',
            'return_from': tomorrow.strftime("%d/%m/%Y"),
            'return_to': half_a_year_later.strftime("%d/%m/%Y"),
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 21
        }

        response = requests.get(url=self.flight_search_endpoint, params=self.parameters, headers=self.header)
        #print(response)
        data = response.json()
        #print(data)

        departure_city_name = data['data'][0]['cityFrom'] 
        departure_city_code = data['data'][0]['cityCodeFrom']
        arrival_city_name = data['data'][0]['cityTo']
        arrival_city_code = data['data'][0]['cityCodeTo']
        outbound_date = data['data'][0]['route'][0]['local_departure'].split("T")[0]
        inbound_date = data['data'][0]['route'][-1]['local_arrival'].split("T")[0]
        flight_price = data['data'][0]['price']
        flight_link = data['data'][0]['deep_link']

        flight_details = {"departure_city_name":departure_city_name, 
                          "departure_city_code":departure_city_code, 
                          "arrival_city_name":arrival_city_name, 
                          "arrival_city_code":arrival_city_code,
                          "outbound_date":outbound_date,
                          "inbound_date":inbound_date,
                          "flight_price":flight_price,
                          "flight_link": flight_link}
        
        print(f"From {departure_city_name} to {arrival_city_name}: ${flight_price}")
        return flight_details