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

file = open("example_data.txt","r+")

lines = file.readlines()

for line in lines:
    wind_speed = line[0:5]
    wind_dir = line[6:9]
    temp = line[10:14]
    humidity = line[15:17]
    pm_one = line[18:21]
    pm_two = line[22:25]
    pm_ten = line[26:29]
    cur_time = line[30:36]
    valid_gps = line[37] == 'A'
    latitude = line[39:48]
    latitude_dir = line[49]
    longitude = line[51:61]
    longitude_dir = line[62]
    date = line[76:78] + '/' + line[74:76] + '/' + line[78:80]

    # replace with SQL query
    print('-- NEW LINE --')
    print('wind_speed = ' + wind_speed)
    print('wind_dir = ' + wind_dir)
    print('temp = ' + temp)
    print('humidity = ' + humidity)
    print('pm_one = ' + pm_one)
    print('pm_two = ' + pm_two)
    print('pm_ten = ' + pm_ten)
    print('cur_time = ' + cur_time)
    print('valid_gps = ' + str(valid_gps))
    print('latitude = ' + latitude)
    print('latitude_dir = ' + latitude_dir)
    print('longitude = ' + longitude)
    print('longitude_dir = ' + longitude_dir)
    print('date = ' + date)

file.close()