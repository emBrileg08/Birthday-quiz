"""
birthday.py
Author: emBrileg08
Credit: NA
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name

monthnum= datetime.today().month
thismonth=month_name[monthnum]
thisday=datetime.today().day

name=input("What is your name?")
month=str(input("What month were you born in?"))
year=int(input("What year were you born?"))
day=int(input("What day were you born?"))

if month=="December" or month=="January" or month=="February":
    season="winter"
elif month=="March" or month=="April" or month=="May":
    season="spring"
elif month=="June" or month=="July" or month=="August":
    season="summer"
else:
    season="fall"
    
if year< 1980:
    age= "stone age"
elif year>=2000:
    age="two thousands"
elif year>=1990:
    age="nineties"
else:
    age="eighties"

if month=="October" and day==31:
    print("You were born on Halloween!")
elif month==thismonth and day==thisday:
   print("Happy birthday!")
else:
    print(str(name)+", you are a "+ season + " baby of the "+ age + ".")
    