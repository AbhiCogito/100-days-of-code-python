import requests as rq
import datetime as dt
import os, smtplib
from dotenv import load_dotenv

load_dotenv()
os.system("clear")

MY_LAT = 28.5355
MY_LONG = 77.3910

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG
}

#Email addresses
my_email = os.getenv("EMAIL_USER", "")
my_password = os.getenv("EMAIL_PASS", "")
send_email = ['gk4ias@gmail.com', 'hcl.priya23@gmail.com', 'singh.abhineet@gmail.com']
assert my_email and my_password, "Missing email credentials in .env file"

def iss_email():
    connection = smtplib.SMTP('smtp.gmail.com', 587)
    connection.ehlo()
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs=send_email, 
                        msg=f"Subject: ISS is above ya! \n\n" \
                        f"The International Space Station is above your location (Noida). \n \
                          Look up!!  ")
    connection.close()

#-----------Converting today's time into 24 hour format-----------#
today = dt.datetime.now()
today_hour = today.strftime('%I')
today_min = today.strftime('%M')
am_pm = today.strftime("%p")

#-----------Fetaching location of ISS-----------------------------#
iss_response = rq.get(url="https://api.wheretheiss.at/v1/satellites/25544")
iss_response.raise_for_status()
iss_lat = float(iss_response.json()['latitude'])
iss_long = float(iss_response.json()['longitude'])

#----------Fetching sunrise & sunset time of given latlong---------#
solar_response = rq.get(url="https://api.sunrise-sunset.org/json", params=parameters)
solar_response.raise_for_status()
sunrise = solar_response.json()['results']['sunrise']
sunset = solar_response.json()['results']['sunset']

#------------Two ways to split a string---------------#
sunrise_temp = sunrise.split(':')
sunrise_hour = int(sunrise_temp[0])
sunrise_min = int(sunrise_temp[1])

sunset_hour, sunset_min, *_ = sunset.split(':')
sunset_hour = int(sunset_hour)
sunset_min = int(sunset_min)

if (MY_LAT-5 <= iss_lat <= MY_LAT+5) and (MY_LONG-5 <= iss_long <= MY_LONG+5) and (am_pm == "PM"):
    iss_email()