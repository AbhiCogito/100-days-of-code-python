import smtplib, random, os
import datetime as dt

os.system("clear")
base_dir = os.path.dirname(os.path.abspath(__file__))
birthdays = os.path.join(base_dir, "birthdays.csv")
letter_1 = os.path.join(base_dir, "letter_templates", "letter_1.txt")
letter_2 = os.path.join(base_dir, "letter_templates", "letter_2.txt")
letter_3 = os.path.join(base_dir, "letter_templates", "letter_3.txt")

letter = [letter_1, letter_2, letter_3]

my_email = "abhineet.exam@gmail.com"
my_password = "daicakkpbexfnaji"

today = dt.datetime.now()
today_month = today.month
today_date = today.day

def birthday_email(name, message):
    connection = smtplib.SMTP('smtp.gmail.com', 587)
    connection.ehlo()
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs="gk4ias@gmail.com", 
                        msg=f"Subject: Hey {name}, Happy Birthday!! \n\n {message}")
    connection.close()

with open(birthdays, 'r') as file:
    dates = file.readlines()

for i in range(len(dates)):
    current_line = dates[i]

    row_data = current_line.strip().split(',')

    try:
        month = int(row_data[3].strip())
        day = int(row_data[4].strip())
        name = row_data[0].strip()
    except Exception:
        continue

    if month == today_month and day == today_date:
        select_letter = random.choice(letter)

        with open(select_letter, 'r') as file:
            message = file.read()

        message = message.replace('[NAME]', name)

        birthday_email(name, message)
