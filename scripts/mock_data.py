
import random
import datetime
import time
import math
# file = open("data.txt", "w")
random.randint(0, 60)

data = []
wind_dir_list = ['N', 'S', 'E', 'W', 'NE', 'SE', 'SW', 'NW']
i = 0
while(i < 10):
    line_data = []
    date = str(datetime.datetime.today()).split()[0]
    line_data.append(date)
    line_data.append(',')
    current_utc = datetime.datetime.utcnow()
    current_utc = current_utc.time().strftime("%H:%M:%S")
    store_cur_time = current_utc
    line_data.append(store_cur_time)
    line_data.append(',')
    humidity = random.randint(50, 90)
    line_data.append(humidity)
    line_data.append(',')
    temp = random.randint(20, 40)
    line_data.append(temp)
    line_data.append(',')
    pm_one = random.randint(0, 60)
    line_data.append(pm_one)
    line_data.append(',')
    pm_two = random.randint(0, 60)
    line_data.append(pm_two)
    line_data.append(',')
    pm_ten = random.randint(0, 60)
    line_data.append(pm_ten)
    line_data.append(',')
    wind_dir = random.randint(0, 7)
    wind_dir = wind_dir_list[wind_dir]
    line_data.append(wind_dir)
    line_data.append(',')
    wind_speed = random.randint(0, 60)
    line_data.append(wind_speed)
    line_data.append('\n')

    line_data = ' '.join(str(v) for v in line_data)
    data.append(line_data)
    print(line_data)
    i += 1
    time.sleep(1)
with open('data.txt', 'w') as f:
    for line in data:
        f.write(line)
