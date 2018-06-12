import requests
import pyodbc
import numpy
import matplotlib.pyplot as plt
import pylab

server = 'DESKTOP-F3EKE9S\ADONISCE30'
uname = 'DESKTOP-F3EKE9S\Matsyk'

cnxn = pyodbc.connect(driver='{SQL Server Native Client 11.0}',host=server, database='baza2', trusted_connection='yes',user=uname)
cursor = cnxn.cursor()


def info():
    cursor.execute("SELECT main.temp, city.name FROM  main, city WHERE main.main_id=city.main_id ORDER BY main.temp DESC")
    max_temp = cursor.fetchall()
    return max_temp[0]


def min_temp():
    cursor.execute("SELECT main.temp, city.name FROM  main, city WHERE main.main_id=city.main_id ORDER BY main.temp DESC")
    max_temp = cursor.fetchall()
    return max_temp[4]

def max_cis():
    cursor.execute("SELECT main.pressure, city.name FROM  main, city WHERE main.main_id=city.main_id ORDER BY main.pressure DESC")
    pressure=cursor.fetchall()
    return pressure[0]

def min_cis():

    cursor.execute("SELECT main.pressure, city.name FROM  main, city WHERE main.main_id=city.main_id ORDER BY main.pressure DESC")
    pressure=cursor.fetchall()
    return pressure[4]

def max_wilg():
    cursor.execute("SELECT main.humidity, city.name FROM  main, city WHERE main.main_id=city.main_id ORDER BY main.humidity DESC")
    humidity=cursor.fetchall()
    return humidity[0]

def min_wilg():
    cursor.execute("SELECT main.humidity, city.name FROM  main, city WHERE main.main_id=city.main_id ORDER BY main.humidity DESC")
    humidity=cursor.fetchall()
    return humidity[4]

def min_zachmurzenie():
    cursor.execute("SELECT clouds.al, city.name FROM clouds,city WHERE clouds.cloud_id=city.cloud_id ORDER BY clouds.al DESC")
    clouds=cursor.fetchall()
    return clouds[4]

def max_zachmurzenie():
    cursor.execute("SELECT clouds.al, city.name FROM clouds,city WHERE clouds.cloud_id=city.cloud_id ORDER BY clouds.al DESC")
    clouds=cursor.fetchall()
    return clouds[0]


def max_wiatr():
    cursor.execute("SELECT city.name, winds.speed FROM city, winds WHERE winds.wind_id=city.wind_id ORDER BY winds.speed DESC")
    wind_speed=cursor.fetchall()
    return wind_speed[0]


def min_wiatr():
    cursor.execute("SELECT city.name, winds.speed FROM city, winds WHERE winds.wind_id=city.wind_id ORDER BY winds.speed DESC")
    wind_speed=cursor.fetchall()
    return wind_speed[4]

def max_res():
    cursor.execute("SELECT city.name,restaurants.name, restaurants.rating FROM city, restaurants WHERE city.id_res=restaurants.res_id ORDER BY restaurants.rating DESC ")
    res=cursor.fetchall()
    return res[0]

def min_res():
    cursor.execute("SELECT city.name,restaurants.name, restaurants.rating FROM city, restaurants WHERE city.id_res=restaurants.res_id ORDER BY restaurants.rating DESC ")
    res=cursor.fetchall()
    return res[4]


def max_park():
    cursor.execute("SELECT park.rating,park.name, city.name FROM city, park WHERE city.park_id=park.park_id ORDER BY park.rating DESC")
    park=cursor.fetchall()
    return park[0]

def min_park():
    cursor.execute("SELECT park.rating,park.name, city.name FROM city, park WHERE city.park_id=park.park_id ORDER BY park.rating DESC")
    park=cursor.fetchall()
    return park[0]

def ogolna():
    cursor.execute("SELECT city.name, weather.description FROM city, weather WHERE city.weather_id=weather.weather_id")
    weather=cursor.fetchall()
    return weather[0]

def ogolna2():
    cursor.execute("SELECT city.name, weather.description FROM city, weather WHERE city.weather_id=weather.weather_id")
    weather=cursor.fetchall()
    return weather[1]

def ogolna3():
    cursor.execute("SELECT city.name, weather.description FROM city, weather WHERE city.weather_id=weather.weather_id")
    weather=cursor.fetchall()
    return weather[2]

def ogolna4():
    cursor.execute("SELECT city.name, weather.description FROM city, weather WHERE city.weather_id=weather.weather_id")
    weather=cursor.fetchall()
    return weather[3]

def ogolna5():
    cursor.execute("SELECT city.name, weather.description FROM city, weather WHERE city.weather_id=weather.weather_id")
    weather=cursor.fetchall()
    return weather[4]

# pobieranie danych z bazy
def temperatura():

    cursor.execute("SELECT main.temp, city.name FROM  main, city WHERE main.main_id=city.main_id ORDER BY main.temp DESC")
    temperatury=cursor.fetchall()
    print(temperatury[0])
    print(temperatury[1])
    print(temperatury[2])
    print(temperatury[3])
    print(temperatury[4])
    x1=temperatury[0]
    x2=temperatury[1]
    x3=temperatury[2]
    x4=temperatury[3]
    x5=temperatury[4]
    #for rec[],rec2[] in temperatury:
    #    print "Print "
        #print(rec[1])
        #print(rec2[1])

    #print cursor.fetchall()

def wszystkie():
    cursor.execute("SELECT main.temp, city.name FROM  main, city WHERE main.main_id=city.main_id ORDER BY main.temp DESC")
    temperatury=cursor.fetchall()
    print("tempteratury")
    print(temperatury[0])
    print(temperatury[1])
    print(temperatury[2])
    print(temperatury[3])
    print(temperatury[4])

    #pressure
    cursor.execute("SELECT main.pressure, city.name FROM  main, city WHERE main.main_id=city.main_id ORDER BY main.pressure DESC")
    pressure=cursor.fetchall()
    print("cisnienie")
    print(pressure[0])
    print(pressure[1])
    print(pressure[2])
    print(pressure[3])
    print(pressure[4])

    #humidity
    cursor.execute("SELECT main.humidity, city.name FROM  main, city WHERE main.main_id=city.main_id ORDER BY main.humidity DESC")
    humidity=cursor.fetchall()
    print("wilgotnosc")
    print(humidity[0])
    print(humidity[1])
    print(humidity[2])
    print(humidity[3])
    print(humidity[4])

    #clouds
    cursor.execute("SELECT clouds.al, city.name FROM clouds,city WHERE clouds.cloud_id=city.cloud_id ORDER BY clouds.al DESC")
    clouds=cursor.fetchall()
    print("chmukrki")
    print(clouds[0])
    print(clouds[1])
    print(clouds[2])
    print(clouds[3])
    print(clouds[4])

    #weather
    cursor.execute("SELECT city.name, weather.description FROM city, weather WHERE city.weather_id=weather.weather_id")
    weather=cursor.fetchall()
    print("ogonie ")
    print(weather[0])
    print(weather[1])
    print(weather[2])
    print(weather[3])
    print(weather[4])

    #wind
    cursor.execute("SELECT city.name, winds.speed FROM city, winds WHERE winds.wind_id=city.wind_id ORDER BY winds.speed DESC")
    wind_speed=cursor.fetchall()
    print("wiatr predkosc")
    print(wind_speed[0])
    print(wind_speed[1])
    print(wind_speed[2])
    print(wind_speed[3])
    print(wind_speed[4])

    #restaurant
    cursor.execute("SELECT city.name,restaurants.name, restaurants.rating FROM city, restaurants WHERE city.id_res=restaurants.res_id ORDER BY restaurants.rating DESC ")
    res=cursor.fetchall()
    print("restaurant")
    print(res[0])
    print(res[1])
    print(res[2])
    print(res[3])
    print(res[4])

    #park
    cursor.execute("SELECT park.rating,park.name, city.name FROM city, park WHERE city.park_id=park.park_id ORDER BY park.rating DESC")
    park=cursor.fetchall()
    print("park")
    print(park[0])
    print(park[1])
    print(park[2])
    print(park[3])
    print(park[4])



def wykresy():
    cursor.execute("SELECT temp FROM main ORDER BY temp DESC ")
    same_temperatury=cursor.fetchall()
    print(same_temperatury[0])
    print(same_temperatury[1])
    print(same_temperatury[2])
    print(same_temperatury[3])
    print(same_temperatury[4])

    s_t1=same_temperatury[0]
    s_t2=same_temperatury[1]
    s_t3=same_temperatury[2]
    s_t4=same_temperatury[3]
    s_t5=same_temperatury[4]

    x=['Warsaw','Rome','Madrit','London','Paris']
    y = [s_t1, s_t2, s_t3, s_t4, s_t5]


    cursor.execute("SELECT pressure FROM  main ORDER BY pressure DESC")
    d_pressure=cursor.fetchall()
    d_p1=d_pressure[0]
    d_p2 = d_pressure[1]
    d_p3 = d_pressure[2]
    d_p4 = d_pressure[3]
    d_p5 = d_pressure[4]

    y2=[d_p1,d_p2,d_p3,d_p4,d_p5]
    x2=['Paris','Rome','Madrit','London','Warsaw']

    cursor.execute("SELECT humidity FROM  main ORDER BY humidity DESC")
    d_humidity=cursor.fetchall()
    d_h1=d_humidity[0]
    d_h2 = d_humidity[1]
    d_h3 = d_humidity[2]
    d_h4 = d_humidity[3]
    d_h5 = d_humidity[4]

    y3=[d_h1,d_h2,d_h3,d_h4,d_h5]
    x3=['Paris','London','Rome','Madrit','Warsaw']
    #clouds
    cursor.execute("SELECT al FROM clouds ORDER BY al DESC")
    d_clouds=cursor.fetchall()
    d_c1=d_clouds[0]
    d_c2 = d_clouds[1]
    d_c3 = d_clouds[2]
    d_c4 = d_clouds[3]
    d_c5 = d_clouds[4]

    y4=[d_c1,d_c2,d_c3,d_c4,d_c5]
    x4=['Paris','London','Madrit','Rome',"Warsaw"]

    #wiatr
    cursor.execute("SELECT speed FROM winds ORDER BY speed DESC")
    d_wind_speed=cursor.fetchall()
    d_w1=d_wind_speed[0]
    d_w2 = d_wind_speed[1]
    d_w3 = d_wind_speed[2]
    d_w4 = d_wind_speed[3]
    d_w5 = d_wind_speed[4]

    y5=[d_w1,d_w2,d_w3,d_w4,d_w5]
    x5=['Warsaw','Paris','Rome','Madrit','London']

    #restaurant
    cursor.execute("SELECT rating FROM restaurants ORDER BY rating DESC ")
    d_res=cursor.fetchall()
    d_r1=d_res[0]
    d_r2 = d_res[1]
    d_r3 = d_res[2]
    d_r4 = d_res[3]
    d_r5 = d_res[4]

    y6=[d_r1,d_r2,d_r3,d_r4,d_r5]
    x6=['Paris','Madrit','Warsaw','London','Rome']


    #park
    cursor.execute("SELECT rating  FROM park  ORDER BY rating DESC")
    d_park=cursor.fetchall()
    d_park1=d_park[0]
    d_park2 = d_park[1]
    d_park3 = d_park[2]
    d_park4 = d_park[3]
    d_park5 = d_park[4]

    y7=[d_park1,d_park2,d_park3,d_park4,d_park5]
    x7=['Warsaw','Paris','Rome','London','Madrit']


    pylab.title('Temperatura')
    pylab.plot(x, y, 'ro')
    pylab.show()

    pylab.title('pressure')
    pylab.plot(x2,y2, 'ro')
    pylab.show()
    pylab.grid(True)

    pylab.title('humidity')
    pylab.plot(x3,y3, 'ro')
    pylab.show()
    pylab.grid(True)

    pylab.title('clouds')
    pylab.plot(x4,y4, 'ro')
    pylab.show()
    pylab.grid(True)

    pylab.title('wind')
    pylab.plot(x5,y5, 'ro')
    pylab.show()
    pylab.grid(True)

    pylab.title('restauant')
    pylab.plot(x6,y6, 'ro')
    pylab.show()
    pylab.grid(True)

    pylab.title('park')
    pylab.plot(x7,y7, 'ro')
    pylab.show()
    pylab.grid(True)



def sun():
    cursor.execute("SELECT sunrise FROM sys")
    sunrise=cursor.fetchall()

    cursor.execute("SELECT sunset FROM sys")
    sunset=cursor.fetchall()

    print(sunrise[0])
#    s_PL[0]=sunset[0]-sunrise[0]
#    print(s_PL[0])


def proba():
    ola="ala"
    return ola
#same_temp()
#temperatura()
#wszystkie()
#sun
info()
