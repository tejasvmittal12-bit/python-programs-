city  = input("Enter Your City Name:")
temp  = float(input("Enter Today's Temperatuer In C:"))

if temp > 35:
    print("Warning: It is very hot today!")

if temp > 25:
        print("Grat day to go outside!")
else:
        print("Grab a jacket before you go out!") 

if temp > 35:
    print ("Weather: Scorching Hot!")
elif temp > 25:
    print ("Weather: Warm and Sunny")
elif temp > 15:
    print ("Weather: Cold and Breezy")
else:
    print ("Weather: Cold- stay warm!")

import datetime
import calendar

now = datetime.datetime.now()
print("City: ", city)
print("Time now:" , now)
print(calendar.calendar(now.year))