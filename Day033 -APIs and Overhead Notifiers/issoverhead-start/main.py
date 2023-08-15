import requests
from datetime import datetime
import smtplib
import time


MY_LAT = 38.722252 # Your latitude
MY_LONG = -9.139337 # Your longitude
MARGIN_OF_ERROR = 5
MY_MAIL = "XXXXXXX"
MY_PASSWORD = "XXXXXXX"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json", verify=False)
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (MY_LAT-MARGIN_OF_ERROR) <= iss_latitude <= (MY_LAT+5) and (MY_LONG-5) <= iss_longitude <= (MY_LONG+5)
        return True
    else:
        return False

def is_night():
    parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters, verify=False)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if time_now >= sunset <= sunrise:
        return True
    else:
        return False

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_MAIL,MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_MAIL,
            to_addrs=MY_MAIL,
            msg="Subject: Lookup 👆\n\nThe ISS is above you in the Sky"
        )




