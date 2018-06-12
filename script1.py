import requests
import pyodbc


server = 'DESKTOP-F3EKE9S\ADONISCE30'
uname = 'DESKTOP-F3EKE9S\Matsyk'

cnxn = pyodbc.connect(driver='{SQL Server Native Client 11.0}',host=server, database='baza2', trusted_connection='yes',user=uname)
cursor = cnxn.cursor()


# Warszawa
api_address_warsaw = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q=Warsaw'
json_data_warsaw = requests.get(api_address_warsaw).json()

sys_country_warsaw=json_data_warsaw['sys']['country']
sys_sunrise_warsaw=json_data_warsaw['sys']['sunrise']
sys_sunset_warsaw=json_data_warsaw['sys']['sunset']

weather_main_warsaw=json_data_warsaw['weather'][0]['main']
weather_description_warsaw = json_data_warsaw['weather'][0]['description']

main_temp_warsaw_kelwin = json_data_warsaw['main']['temp']
temp_warsaw = main_temp_warsaw_kelwin - 273
main_pressure_warsaw = json_data_warsaw['main']['pressure']
main_humidity_warsaw = json_data_warsaw['main']['humidity']

wind_speed_warsaw = json_data_warsaw['wind']['speed']

clouds_warsaw=json_data_warsaw['clouds']['all']

#wawa rystauracje
api_address_restaurant_warsaw='https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=52.22967560,21.012228702&radius=40000&type=restaurant&keyword=cruise&key=AIzaSyBszOfV1qwPGfdTfqYhmqtKy4ER-tItP88'
api_address_park_warsaw='https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=52.22967560,21.012228702&radius=40000&type=zoo&keyword=cruise&key=AIzaSyBszOfV1qwPGfdTfqYhmqtKy4ER-tItP88'
json_data_r_w = requests.get(api_address_restaurant_warsaw).json()
json_data_p_w = requests.get(api_address_park_warsaw).json()

#Warsaw

restaurant1=json_data_r_w['results'][0]['name']
restaurant1_rating=json_data_r_w['results'][0]['rating']
restaurant2=json_data_r_w['results'][1]['name']
restaurant3=json_data_r_w['results'][2]['name']
park1=json_data_p_w['results'][0]['name']
park1_w=json_data_p_w['results'][0]['rating']

print("Warsaw:")
print("weather_main",weather_main_warsaw)
print("description", weather_description_warsaw)
print("temp", temp_warsaw)
print("weather pressure", main_pressure_warsaw)
print("humidity", main_humidity_warsaw)
print("wind speed", wind_speed_warsaw)
print("system",sys_country_warsaw,sys_sunrise_warsaw,sys_sunset_warsaw)
print("clouds", clouds_warsaw)


print('Warsaw')
print(restaurant1)
print(restaurant2)
print(restaurant3)
print(park1)



command = "insert into sys (sys_id, country, sunrise, sunset)  values (?, ?, ?, ?)"
parameters = ["1", sys_country_warsaw, sys_sunrise_warsaw, sys_sunset_warsaw]
cursor.execute(command, parameters)

command = "insert into weather (weather_id, main, description)  values (?, ?, ?)"
parameters = ["1",weather_main_warsaw,weather_description_warsaw]
cursor.execute(command, parameters)

command = "insert into main (main_id, temp, pressure, humidity)  values (?, ?, ?, ?)"
parameters = ["1", temp_warsaw, main_pressure_warsaw, main_humidity_warsaw]
cursor.execute(command, parameters)

command = "insert into winds (wind_id, speed)  values (?, ?)"
parameters = ["1", wind_speed_warsaw]
cursor.execute(command, parameters)

command = "insert into clouds (cloud_id, al)  values (?, ?)"
parameters = ["1", clouds_warsaw]
cursor.execute(command, parameters)

command = "insert into restaurants (res_id, name, rating)  values (?, ?, ?)"
parameters = ["1", restaurant1,restaurant1_rating]
cursor.execute(command, parameters)


command = "insert into park (park_id, name, rating)  values (?, ?, ?)"
parameters = ["1", park1, park1_w]
cursor.execute(command, parameters)



# London
api_address_london = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q=London'
json_data_london = requests.get(api_address_london).json()

sys_country_london=json_data_london['sys']['country']
sys_sunrise_london=json_data_london['sys']['sunrise']
sys_sunset_london=json_data_london['sys']['sunset']

weather_main_london=json_data_london['weather'][0]['main']
weather_description_london = json_data_london['weather'][0]['description']

main_temp_london_kelwin = json_data_london['main']['temp']
temp_london = main_temp_london_kelwin - 273
main_pressure_london = json_data_london['main']['pressure']
main_humidity_london = json_data_london['main']['humidity']

wind_speed_london = json_data_london['wind']['speed']

clouds_london=json_data_london['clouds']['all']

#London rystauracje

api_address_restaurant_london='https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=51.509865,-0.118092&radius=1000&type=restaurant&keyword=cruise&key=AIzaSyBszOfV1qwPGfdTfqYhmqtKy4ER-tItP88'
api_address_park_london='https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=51.509865,-0.118092&radius=40000&type=zoo&keyword=cruise&key=AIzaSyBszOfV1qwPGfdTfqYhmqtKy4ER-tItP88'
json_data_r_l = requests.get(api_address_restaurant_london).json()
json_data_p_l = requests.get(api_address_park_london).json()
restaurant4=json_data_r_l['results'][0]['name']
restaurant1_rating_london=json_data_r_l['results'][0]['rating']
restaurant5=json_data_r_l['results'][1]['name']
restaurant6=json_data_r_l['results'][2]['name']
park2=json_data_p_l['results'][0]['name']
park1_l=json_data_p_l['results'][0]['rating']



print("London:")
print("weather_main",weather_main_london)
print("description", weather_description_london)
print("temp", temp_london)
print("weather pressure", main_pressure_london)
print("humidity", main_humidity_london)
print("wind speed", wind_speed_london)
print("system",sys_country_london,sys_sunrise_london,sys_sunset_london)
print("clouds", clouds_london)

print("London")
print(restaurant4)
print(restaurant5)
print(restaurant6)
print(park2)

command = "insert into sys (sys_id, country, sunrise, sunset)  values (?, ?, ?, ?)"
parameters = ["2", sys_country_london, sys_sunrise_london, sys_sunset_london]
cursor.execute(command, parameters)

command = "insert into weather (weather_id, main, description)  values (?, ?, ?)"
parameters = ["2",weather_main_london,weather_description_london]
cursor.execute(command, parameters)

command = "insert into main (main_id, temp, pressure, humidity)  values (?, ?, ?, ?)"
parameters = ["2", temp_london, main_pressure_london, main_humidity_london]
cursor.execute(command, parameters)

command = "insert into winds (wind_id, speed)  values (?, ?)"
parameters = ["2", wind_speed_london]
cursor.execute(command, parameters)

command = "insert into clouds (cloud_id, al)  values (?, ?)"
parameters = ["2", clouds_london]
cursor.execute(command, parameters)

command = "insert into restaurants (res_id, name, rating)  values (?, ?, ?)"
parameters = ["2", restaurant4,restaurant1_rating_london]
cursor.execute(command, parameters)


command = "insert into park (park_id, name, rating)  values (?, ?, ?)"
parameters = ["2", park2, park1_l]
cursor.execute(command, parameters)

# Paris
api_address_paris = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q=Paris'
json_data_paris = requests.get(api_address_paris).json()

sys_country_paris=json_data_paris['sys']['country']
sys_sunrise_paris=json_data_paris['sys']['sunrise']
sys_sunset_paris=json_data_paris['sys']['sunset']

weather_main_paris=json_data_paris['weather'][0]['main']
weather_description_paris = json_data_paris['weather'][0]['description']

main_temp_paris_kelwin = json_data_paris['main']['temp']
temp_paris = main_temp_paris_kelwin - 273
main_pressure_paris = json_data_paris['main']['pressure']
main_humidity_paris = json_data_paris['main']['humidity']

wind_speed_paris = json_data_paris['wind']['speed']

clouds_paris=json_data_paris['clouds']['all']

#Paris restaurant
api_address_restaurant_paris='https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=48.864716,2.349014&radius=40000&type=restaurant&keyword=cruise&key=AIzaSyBszOfV1qwPGfdTfqYhmqtKy4ER-tItP88'
api_address_park_paris='https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=48.864716,2.349014&radius=40000&type=park&keyword=cruise&key=AIzaSyBszOfV1qwPGfdTfqYhmqtKy4ER-tItP88'
json_data_r_paris = requests.get(api_address_restaurant_paris).json()
json_data_p_paris = requests.get(api_address_park_paris).json()
restaurant7=json_data_r_paris['results'][0]['name']
restaurant1_rating_paris=json_data_r_paris['results'][0]['rating']
restaurant8=json_data_r_paris['results'][1]['name']
restaurant9=json_data_r_paris['results'][2]['name']
park3=json_data_p_paris['results'][0]['name']
park1_p=json_data_p_paris['results'][0]['rating']

print("Paris:")
print("weather_main",weather_main_paris)
print("description", weather_description_paris)
print("temp", temp_paris)
print("weather pressure", main_pressure_paris)
print("humidity", main_humidity_paris)
print("wind speed", wind_speed_paris)
print("system",sys_country_paris,sys_sunrise_paris,sys_sunset_paris)
print("clouds", clouds_paris)

print("Paris")
print(restaurant7)
print(restaurant8)
print(restaurant9)
print(park3)

command = "insert into sys (sys_id, country, sunrise, sunset)  values (?, ?, ?, ?)"
parameters = ["3", sys_country_paris, sys_sunrise_paris, sys_sunset_paris]
cursor.execute(command, parameters)

command = "insert into weather (weather_id, main, description)  values (?, ?, ?)"
parameters = ["3",weather_main_paris,weather_description_paris]
cursor.execute(command, parameters)

command = "insert into main (main_id, temp, pressure, humidity)  values (?, ?, ?, ?)"
parameters = ["3", temp_paris, main_pressure_paris, main_humidity_paris]
cursor.execute(command, parameters)

command = "insert into winds (wind_id, speed)  values (?, ?)"
parameters = ["3", wind_speed_paris]
cursor.execute(command, parameters)

command = "insert into clouds (cloud_id, al)  values (?, ?)"
parameters = ["3", clouds_paris]
cursor.execute(command, parameters)

command = "insert into restaurants (res_id, name, rating)  values (?, ?, ?)"
parameters = ["3", restaurant1,restaurant1_rating_paris]
cursor.execute(command, parameters)


command = "insert into park (park_id, name, rating)  values (?, ?, ?)"
parameters = ["3", park3, park1_p]
cursor.execute(command, parameters)

# Rome
api_address_rome = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q=Rome'
json_data_rome = requests.get(api_address_rome).json()

sys_country_rome=json_data_rome['sys']['country']
sys_sunrise_rome=json_data_rome['sys']['sunrise']
sys_sunset_rome=json_data_rome['sys']['sunset']

weather_main_rome=json_data_rome['weather'][0]['main']
weather_description_rome = json_data_rome['weather'][0]['description']

main_temp_rome_kelwin = json_data_rome['main']['temp']
temp_rome = main_temp_rome_kelwin - 273
main_pressure_rome = json_data_rome['main']['pressure']
main_humidity_rome = json_data_rome['main']['humidity']

wind_speed_rome = json_data_rome['wind']['speed']

clouds_rome=json_data_rome['clouds']['all']



api_address_restaurant_roma ='https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=41.890251,12.492373&radius=40000&type=bar&keyword=cruise&key=AIzaSyBszOfV1qwPGfdTfqYhmqtKy4ER-tItP88'
api_address_park_roma ='https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=41.89193,12.51133&radius=40000&type=zoo&keyword=cruise&key=AIzaSyBszOfV1qwPGfdTfqYhmqtKy4ER-tItP88'
json_data_r_roma = requests.get(api_address_restaurant_roma).json()
json_data_p_roma = requests.get(api_address_park_roma).json()
restaurant10=json_data_r_roma['results'][0]['name']
restaurant1_rating_roma=json_data_r_roma['results'][0]['rating']
restaurant11=json_data_r_roma['results'][1]['name']
restaurant12=json_data_r_roma['results'][2]['name']
park4=json_data_p_roma['results'][0]['name']
park1_r=json_data_p_roma['results'][0]['rating']

print("Rome:")
print("weather_main",weather_main_rome)
print("description", weather_description_rome)
print("temp", temp_rome)
print("weather pressure", main_pressure_rome)
print("humidity", main_humidity_rome)
print("wind speed", wind_speed_rome)
print("system",sys_country_rome,sys_sunrise_rome,sys_sunset_rome)
print("clouds", clouds_rome)

print("Rome")
print(restaurant10)
print(restaurant11)
print(restaurant12)
print(park4)


command = "insert into sys (sys_id, country, sunrise, sunset)  values (?, ?, ?, ?)"
parameters = ["4", sys_country_rome, sys_sunrise_rome, sys_sunset_rome]
cursor.execute(command, parameters)

command = "insert into weather (weather_id, main, description)  values (?, ?, ?)"
parameters = ["4",weather_main_rome,weather_description_rome]
cursor.execute(command, parameters)

command = "insert into main (main_id, temp, pressure, humidity)  values (?, ?, ?, ?)"
parameters = ["4", temp_rome, main_pressure_rome, main_humidity_rome]
cursor.execute(command, parameters)

command = "insert into winds (wind_id, speed)  values (?, ?)"
parameters = ["4", wind_speed_rome]
cursor.execute(command, parameters)

command = "insert into clouds (cloud_id, al)  values (?, ?)"
parameters = ["4", clouds_rome]
cursor.execute(command, parameters)

command = "insert into restaurants (res_id, name, rating)  values (?, ?, ?)"
parameters = ["4", restaurant10,restaurant1_rating_roma]
cursor.execute(command, parameters)


command = "insert into park (park_id, name, rating)  values (?, ?, ?)"
parameters = ["4", park4, park1_r]
cursor.execute(command, parameters)


# Mardid
api_address_madrid = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q=Madrid'
json_data_madrid= requests.get(api_address_madrid).json()

sys_country_madrid=json_data_madrid['sys']['country']
sys_sunrise_madrid=json_data_madrid['sys']['sunrise']
sys_sunset_madrid=json_data_madrid['sys']['sunset']

weather_main_madrid=json_data_madrid['weather'][0]['main']
weather_description_madrid = json_data_madrid['weather'][0]['description']

main_temp_madrid_kelwin = json_data_madrid['main']['temp']
temp_madrid = main_temp_madrid_kelwin - 273
main_pressure_madrid = json_data_madrid['main']['pressure']
main_humidity_madrid = json_data_madrid['main']['humidity']

wind_speed_madrid = json_data_madrid['wind']['speed']

clouds_madrid=json_data_madrid['clouds']['all']

#Madrit restaurant
api_address_restaurant_madrit='https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=40.4165,-3.70256&radius=40000&type=restaurant&keyword=cruise&key=AIzaSyBszOfV1qwPGfdTfqYhmqtKy4ER-tItP88'
api_address_park_madrit='https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=40.4165,-3.70256&radius=40000&type=park&keyword=cruise&key=AIzaSyBszOfV1qwPGfdTfqYhmqtKy4ER-tItP88'
json_data_r_madrit = requests.get(api_address_restaurant_madrit).json()
json_data_p_madrit = requests.get(api_address_park_madrit).json()
restaurant13=json_data_r_madrit['results'][0]['name']
restaurant1_rating_madrit=json_data_r_madrit['results'][0]['rating']
restaurant14=json_data_r_madrit['results'][1]['name']
restaurant15=json_data_r_madrit['results'][2]['name']
park5=json_data_p_madrit['results'][0]['name']
park1_m=json_data_p_madrit['results'][0]['rating']
print("Madrid:")
print("weather_main",weather_main_madrid)
print("description", weather_description_madrid)
print("temp", temp_madrid)
print("weather pressure", main_pressure_madrid)
print("humidity", main_humidity_madrid)
print("wind speed", wind_speed_madrid)
print("system",sys_country_madrid,sys_sunrise_madrid,sys_sunset_madrid)
print("clouds", clouds_madrid)

print("Madrit")
print(restaurant13)
print(restaurant14)
print(restaurant15)
print(park5)


command = "insert into sys (sys_id, country, sunrise, sunset)  values (?, ?, ?, ?)"
parameters = ["5", sys_country_madrid, sys_sunrise_madrid, sys_sunset_madrid]
cursor.execute(command, parameters)

command = "insert into weather (weather_id, main, description)  values (?, ?, ?)"
parameters = ["5",weather_main_madrid,weather_description_madrid]
cursor.execute(command, parameters)

command = "insert into main (main_id, temp, pressure, humidity)  values (?, ?, ?, ?)"
parameters = ["5", temp_madrid, main_pressure_madrid, main_humidity_madrid]
cursor.execute(command, parameters)

command = "insert into winds (wind_id, speed)  values (?, ?)"
parameters = ["5", wind_speed_madrid]
cursor.execute(command, parameters)

command = "insert into clouds (cloud_id, al)  values (?, ?)"
parameters = ["5", clouds_madrid]
cursor.execute(command, parameters)

command = "insert into restaurants (res_id, name, rating)  values (?, ?, ?)"
parameters = ["5", restaurant13,restaurant1_rating_madrit]
cursor.execute(command, parameters)


command = "insert into park (park_id, name, rating)  values (?, ?, ?)"
parameters = ["5", park5, park1_m]
cursor.execute(command, parameters)


cnxn.commit()
cnxn.close()
