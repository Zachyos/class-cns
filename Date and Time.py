import os
os.system('cls')
import datetime as obj_dt
birth_date = obj_dt.datetime(2004, 6, 1)
date_now=obj_dt.datetime.now()
print(f"your birthday is {birth_date}")
print(f"The curent date/time is {date_now}")
birthday=date_now - birth_date
print (f"I have been alive and kicken for {birthday.days:,} days")
print (f"I have been alive for {birthday.days*86400:,} seconds...")
print(f"I have been alive for {birthday.days/364.2425:.3f} years now")