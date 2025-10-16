import datetime as dt
import smtplib

my_email = "abhineet.exam@gmail.com"
my_password = "daicakkpbexfnaji"
send_email = ['gk4ias@gmail.com', 'hcl.priya23@gmail.com']

sophie_bdy = dt.date(2020, 10, 25)
milestone = [i for i in range (100, 50000, 100)]
today = dt.datetime.now()

diff = today.date() - sophie_bdy
diff_days = diff.days
# diff_month = diff.

def birthday_email(days):
    connection = smtplib.SMTP('smtp.gmail.com', 587)
    connection.ehlo()
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs=send_email, 
                        msg=f"Subject: Sophie is {days} old!! Celebrate!!! \n\n Sophie turns {days} days old tomorrow.")
    connection.close()

if (diff_days + 1) in milestone:
    birthday_email(diff_days)


