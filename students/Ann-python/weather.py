#pip install pyowm

import pyowm

#Language = "ru"
owm = pyowm.OWM('5cb7882eacb885fc916f21ef03182e00')

place = input("В каком городе/стране? - ")

observation = owm.weather_at_place('place')
w = observation.get_weather()

temp = w.get_temperature('celsius')["temp"]

print ( "В городе " + place + " сейчас " + w.get_detailed_status())
print ( "Температура сейчас - " + str(temp))

if temp < 10:
    print ( "Сейчас ооочень холодно!!!" )
elif temp < 20:
    print ( "Сейчас холодно!" )
else:
    print ( "Температура нормас))" )
    

