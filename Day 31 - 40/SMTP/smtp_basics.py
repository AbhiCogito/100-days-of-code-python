import smtplib, random, os
import datetime as dt

os.system("clear")
base_dir = os.path.dirname(os.path.abspath(__file__))
data = os.path.join(base_dir, "quotes.txt")

my_email = "abhineet.exam@gmail.com"
my_password = "daicakkpbexfnaji"

def email_quote(quote):
    connection = smtplib.SMTP('smtp.gmail.com', 587)
    connection.ehlo()
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs="gk4ias@gmail.com", 
                        msg=f"Subject: Python_email Testing python using VSCode \n\n {quote}")
    connection.close()

with open(data, 'r') as file:
    quotes = file.readlines()

today = dt.datetime.now()
weekday = today.weekday()

if weekday == 0:
    email_quote(random.choice(quotes))








