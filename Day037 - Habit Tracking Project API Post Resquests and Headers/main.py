# Created by Ricardo Lousada
import requests
from datetime import datetime

TOKEN = "MY_TOKEN"
USER = "MY_USER"
GRAPH_ID = "MY_GRAPH_ID"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USER,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Do only once to create the user
response = requests.post(url=pixela_endpoint,json=user_params,verify=False)
print(response.text)

# create graph - Do only once

graph_endpoint = f"{pixela_endpoint}/{USER}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "my_graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}


response = requests.post(url=graph_endpoint,headers=headers, json=graph_params,verify=False)
print(response.text)

# Create a pixel

pixel_creation_endpoint = f"{pixela_endpoint}/{USER}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_date = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("how many QTD to create? ")
}

response = requests.post(url=pixel_creation_endpoint,json=pixel_date,headers=headers, verify=False)
print(response.text)

# Update a pixel

today = datetime.now()
formatted_date = today.strftime("%Y%m%d")

pixel_change_endpoint = f"{pixela_endpoint}/{USER}/graphs/{GRAPH_ID}/{formatted_date}"

pixel_update = {
    "quantity": "10",
}

response = requests.put(url=pixel_change_endpoint, json=pixel_update, headers=headers, verify=False)
print(response.text)

# delete a pixel

today = datetime.now()
formatted_date = today.strftime("%Y%m%d")

pixel_delete_endpoint = f"{pixela_endpoint}/{USER}/graphs/{GRAPH_ID}/{formatted_date}"


response = requests.delete(url=pixel_delete_endpoint, headers=headers, verify=False)
print(response.text)