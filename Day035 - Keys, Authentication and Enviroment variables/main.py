# Created by Ricardo Lousada
import requests
import os
from twilio.rest import Client

API_KEY = "IZ7lT43iAlOftAGecaTkz9wAwhsQMgCI"


URL = "https://api.tomorrow.io/v4/weather/forecast"

headers = {
    "accept": "application/data.json",
    "location": "Lisbon"
}

parameters = {
    "timesteps": "hourly",
    "location": "Lisbon",
    "units":"metric",
    "apikey": API_KEY
}

response = requests.get(URL, headers=headers, verify=False, params=parameters)
response.raise_for_status()
weather_data = response.json()

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Olá Ricardo",
                     from_='+16188674257',
                     to='+351962017185'
                 )

print(message.status)


"""
Whatsapp code
# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body='This is a WhatsApp message sent with Twilio!',
                     from_='whatsapp:+15555238886',
                     to='whatsapp:+15557770006'
                 )

print(message.sid)
"""