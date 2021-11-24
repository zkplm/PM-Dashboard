# data is arranged in txt file as follows:
# wind speed in mph, wind direction out of 360 degrees, temperature in F, humidity, PM1.0, PM2.5, PM10, NMEA-0183 sentence
#
# NMEA-0183 sentence is arranged as follows:
# The sentence type
# Current time (if available; UTC)
# Position status (A for valid, V for invalid)
# Latitude (in DDMM.MMM format)
# Latitude compass direction
# Longitude (in DDDMM.MMM format)
# Longitude compass direction
# Speed (in knots per hour)
# Heading
# Date (DDMMYY)
# Magnetic variation
# Magnetic variation direction
# The checksum validation value (in hexadecimal)

from datetime import datetime
import mysql.connector
import pandas as pd
import time


def find_wind_dir(string_wind):
    if (string_wind == ' N '):
        return 0
    elif string_wind == ' S ':
        return 1
    elif string_wind == ' E ':
        return 2
    elif string_wind == ' W ':
        return 3
    elif string_wind == ' SE ':
        return 4
    elif string_wind == ' SW ':
        return 5
    elif string_wind == ' NW ':
        return 6
    elif string_wind == ' NE ':
        return 7


def file_parser():
    t0 = time.time()
    df = pd.read_csv("Parser/data.txt", header=None)
    valid_gps = None
    latitude = None
    latitude_dir = None
    longitude = None
    longitude_dir = None
    mydb = mysql.connector.connect(
        host="104.197.43.121",
        user="root",
        password="ece445",
        database="PMDATA"
    )
    mycursor = mydb.cursor()
    data = []
    i = 1
    for index, row in df.iterrows():
        date = row[0]
        i += 1
        store_cur_time = str(row[1])
        humidity = str(row[2])
        temp = str(row[3])
        pm_one = str(row[4])
        pm_two = str(row[5])
        pm_ten = str(row[6])
        wind_dir = str(row[7])
        wind_speed = str(row[8])
        wind_convert = str(find_wind_dir(wind_dir))
        val = (wind_speed, wind_dir, temp, humidity, pm_one, pm_two, pm_ten, store_cur_time,
               valid_gps, latitude, latitude_dir, longitude, longitude_dir, date, wind_convert)
        data.append(val)

    sql = "INSERT INTO PM_Data Values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    mycursor.executemany(sql, data)
    mydb.commit()
    t1 = time.time()
    str2 = "Parsed " + str(i) + " rows of data."
    print(str2)
    print("total time (in seconds) to parse data was:", t1-t0)


file_parser()
