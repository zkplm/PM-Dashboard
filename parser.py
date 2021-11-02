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


def file_parser():
    file = open("Parser/data.txt", "r+")

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
        # convert time from string to UTC
        cur_time = datetime.strptime(cur_time, '%H%M%S')
        print(cur_time.time())
        data['time'].append(cur_time.time())

        valid_gps = line[34] == 'A'
        latitude = line[36:45]
        latitude_dir = line[46]
        longitude = line[48:58]
        longitude_dir = line[59]
        date = line[73:75] + '/' + line[71:73] + '/' + line[75:77]

        # replace with SQL query
        print('-- NEW LINE --')
        print('wind_speed = ' + wind_speed)
        print('wind_dir = ' + wind_dir)
        print('temp = ' + temp)
        print('humidity = ' + humidity)
        print('pm_one = ' + pm_one)
        print('pm_two = ' + pm_two)
        print('pm_ten = ' + pm_ten)
        print(cur_time.time())
        print('valid_gps = ' + str(valid_gps))
        print('latitude = ' + latitude)
        print('latitude_dir = ' + latitude_dir)
        print('longitude = ' + longitude)
        print('longitude_dir = ' + longitude_dir)
        print('date = ' + date)

    file.close()
    return data
