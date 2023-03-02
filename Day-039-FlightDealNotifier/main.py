#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager


data = DataManager()
search = FlightSearch()
flight_data = FlightData()
notify = NotificationManager()

sheet_data = data.get_sheet_data()['prices']

for row in sheet_data:
    if row['iataCode'] == '':
        row['iataCode'] = search.get_iata_code(row['city'])

    data.send_row_data(row)

for row in sheet_data:
    flight_details = flight_data.find_deal(row['iataCode'])

    if int(flight_details['flight_price']) < row['lowestPrice']:
        notify.send_mail(flight_details)