import requests
from datetime import datetime
import smtplib

MY_LAT = 33.748997 # Your latitude
MY_LONG = -84.387985 # Your longitude

MY_EMAIL = "tloatmancodes@gmail.com"
MY_PASSWORD = "Peyton030%"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# iss_position = (iss_latitude, iss_longitude)
#
# my_position = (MY_LAT, MY_LONG)

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response2 = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response2.raise_for_status()
data2 = response2.json()
sunrise = int(data2["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data2["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now().hour


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
#

if time_now >= sunset:
    if iss_latitude and MY_LAT in range(MY_LAT - 5, MY_LAT + 5) and iss_longitude and MY_LONG in \
            range(MY_LONG - 5, MY_LONG + 5):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="tloatman77@gmail.com",
                msg=f"Subject:Look Up!\n\nLook Up!!! This ISS is in the sky!!!!"
            )






