import smtplib
from email.message import EmailMessage
import datetime as dt
import random

my_email = "automatedsender2@gmail.com"
test_email = "bcao@vassar.edu.com"
password = "sozd znqf fxrn myqp"

msg = EmailMessage()

def grab_day(weekday):
    if weekday == 0:
        weekday = 'Sunday'
    elif weekday == 1:
        weekday = 'Monday'
    elif weekday == 1:
        weekday = 'Tuesday'
    elif weekday == 1:
        weekday = 'Wednesday'
    elif weekday == 1:
        weekday = 'Thursday'
    elif weekday == 1:
        weekday = 'Friday'
    elif weekday == 1:
        weekday = 'Saturday'
    return weekday

def grab_quote():
    with open("SMTP\quotes.txt") as quote_files:
        quotes = quote_files.readlines()
        random_quote = random.randint(0, len(quotes))
        quote = quotes[random_quote]
        return quote

def send_email(subject, content):
    msg.set_content(content)
    msg['Subject'] = subject
    msg['From'] = my_email
    msg['To'] = test_email

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.send_message(msg)

date = dt.datetime.now()
month = date.month
day = date.day 
year = date.year 
weekday = grab_day(date.weekday())

print(f"{month}/{day}/{year} - {weekday}")

birthday = dt.datetime(year= 2001, month= 11, day = 1)
print(birthday)

quote = grab_quote()

send_email("Inspiration!", quote)