import requests
from datetime import datetime
import smtplib

MY_LAT = 52.110460 # Your latitude
MY_LONG = 21.270100 # Your longitude

my_email = "antycwel12@gmail.com"
password = "dbiv movo zypy nanh"
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude =float(data["iss_position"]["latitude"])
iss_longitude =float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
def cord_check():
    if MY_LAT-5<=iss_latitude<=MY_LAT+5 and MY_LONG-5<=iss_longitude<=MY_LONG+5:
        if  int(time_now.hour)>=sunset or int(time_now.hour)<=sunrise:
            send()

def send():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg="Subject:  Look UP!!!!\n\n beka z cb ze patrzysz teraz ci hakuje kompa"
                            )

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
cord_check()
#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



