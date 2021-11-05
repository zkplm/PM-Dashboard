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


def file_parser():
    file = open("Parser/data.txt", "r+")
    mydb = mysql.connector.connect(
        host="104.197.43.121",
        user="root",
        password="ece445",
        database="PMDATA"
    )
    mycursor = mydb.cursor()
    lines = file.readlines()
    data = {}
    data['time'] = []
    data['PM1'] = []
    data['PM2.5'] = []
    data['PM10'] = []
    for line in lines:
        wind_speed = line[0:5]
        wind_dir = line[6:9]
        temp = line[10:14]
        humidity = line[15:17]
        pm_one = line[18:20]

        data['PM1'].append(int(pm_one))
        pm_two = line[21:23]

        data['PM2.5'].append(int(pm_two))
        pm_ten = line[24:26]

        data['PM10'].append(int(pm_ten))
        cur_time = line[27:33]
        store_cur_time = line[27:33]
        # convert time from string to UTC
        print(cur_time)
        cur_time = datetime.strptime(cur_time, '%H%M%S')
        print(cur_time.time())
        data['time'].append(cur_time.time())

        valid_gps = line[34] == 'A'
        latitude = line[36:45]
        latitude_dir = line[46]
        longitude = line[48:58]
        longitude_dir = line[59]
        date = line[73:75] + '/' + line[71:73] + '/' + line[75:77]

        # insert into DB
        sql = "INSERT INTO PM_Data Values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (wind_speed, wind_dir, temp, humidity, pm_one, pm_two, pm_ten, store_cur_time,
               valid_gps, latitude, latitude_dir, longitude, longitude_dir, date)
        mycursor.execute(sql, val)
        mydb.commit()
        # replace with SQL query
        # print('-- NEW LINE --')
        # print('wind_speed = ' + wind_speed)
        # print('wind_dir = ' + wind_dir)
        # print('temp = ' + temp)
        # print('humidity = ' + humidity)
        # print('pm_one = ' + pm_one)
        # print('pm_two = ' + pm_two)
        # print('pm_ten = ' + pm_ten)
        # print(cur_time.time())
        # print('valid_gps = ' + str(valid_gps))
        # print('latitude = ' + latitude)
        # print('latitude_dir = ' + latitude_dir)
        # print('longitude = ' + longitude)
        # print('longitude_dir = ' + longitude_dir)
        # print('date = ' + date)
    print(data)
    file.close()
    return data


# file_parser()
