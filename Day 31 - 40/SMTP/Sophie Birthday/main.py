import datetime as dt
import smtplib, os
from dotenv import load_dotenv

#Email addresses
my_email = os.getenv("EMAIL_USER", "")
my_password = os.getenv("EMAIL_PASS", "")
send_email = ['gk4ias@gmail.com', 'hcl.priya23@gmail.com', 'singh.abhineet@gmail.com']

#Working with dates
sophie_bdy = dt.date(2020, 10, 25)
milestone = [i for i in range (100, 50000, 100)]
today = dt.datetime.now()

diff = today.date() - sophie_bdy
diff_days = diff.days
diff_year = today.year - sophie_bdy.year

def birthday_email(days):
    connection = smtplib.SMTP('smtp.gmail.com', 587)
    connection.ehlo()
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs=send_email, 
                        msg=f"Subject: Sophie is {days} days old!! Celebrate!!! \n\n" \
                        f"Sophie turns {days} days old tomorrow. \n" \
                        f"Invest {diff_year*1000} per month in mutual funds.\n" \
                        f"Be a responsible parent please. Her future is dependent on you.")
    connection.close()

#Sending the email one day before the milestone occurs
if (diff_days + 1) in milestone:
    birthday_email(diff_days)


