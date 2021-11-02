
import random
import datetime
import time
import math
#file = open("data.txt", "w")

data = []
i = 0
while(i < 10):
    line_data = '015.5 120 72.2 55 '
    PM1 = random.randint(0, 60)
    PM25 = random.randint(0, 60)
    PM10 = random.randint(0, 60)
    current_utc = datetime.datetime.utcnow()
    current_utc = current_utc.time().strftime("%H%M%S")
    line_data = line_data + str(PM1) + ' '
    line_data = line_data + str(PM25) + ' '
    line_data = line_data + str(PM10) + ' '
    line_data = line_data + \
        str(current_utc) + ',A,3855.4487,N,09446.0071,W,0.0,076.2,130495,003.8,E*69'
    line_data += '\n'
    data.append(line_data)
    print(line_data)
    i += 1
    time.sleep(1)
with open('data.txt', 'w') as f:
    for line in data:
        f.write(line)
