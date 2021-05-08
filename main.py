import requests
import os
from datetime import datetime

USERNAME= os.environ["USERNAME"]
TOKEN = os.environ["TOKEN"]
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.today().strftime("%Y%m%d")

pixel_data = {
    "date": "20210507",
    "quantity": "8.86"
}


# response = requests.post(url=pixel_endpoint, json=pixel_data, headers=headers)
# print(response.text)

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20210507"

new_data = {
    "quantity": "6.43",
}

# response = requests.put(url=update_pixel_endpoint, json=new_data, headers=headers)
# print(response.text)

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20210507"

response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)