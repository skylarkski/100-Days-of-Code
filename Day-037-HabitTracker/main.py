import requests
import datetime

pixela_endpoint = "https://pixe.la/v1/users"

#API TOKEN
TOKEN = "YOURTOKENHERE"

USERNAME = "YOURUSERNAMEHERE"
GRAPH_ID = "graph1"

headers = {
    "X-USER-TOKEN": TOKEN
}

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_config = {
    "id": GRAPH_ID,
    "name": "Reading Graph",
    "unit": "pages",
    "type": "int",
    "color": "ajisai"
}

#Using strftime() to format the date
today = datetime.date.today().strftime("%Y%m%d")


def create_account():
    response = requests.post(url=pixela_endpoint, json=user_params)
    print(response.text)


def create_graph():
    graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
    response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
    print(response.text)


def post_pixel_graph(date_to_post, quantity):
    pixel_post_data = {
        'date': date_to_post,
        'quantity': quantity
    }
    pixel_reading_post_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
    response = requests.post(url=pixel_reading_post_endpoint, json=pixel_post_data, headers=headers)
    print(response.text)


def put_pixel_graph(date_to_update, quantity):
    pixel_put_data = {
        'date': date_to_update,
        'quantity': quantity
    }
    pixel_reading_put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_to_update}"
    response = requests.put(url=pixel_reading_put_endpoint, json=pixel_put_data, headers=headers)
    print(response.text)


def delete_pixel_graph(date_to_delete):
    pixel_reading_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date_to_delete}"
    response = requests.delete(url=pixel_reading_delete_endpoint, headers=headers)
    print(response.text)
