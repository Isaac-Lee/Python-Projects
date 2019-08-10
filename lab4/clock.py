import time
t = time.time()
day = int(t)/60*60*24
hour = (int(t)-day*60*60*24)/60*60
minute = (int(t)-((day*60*60*24)+(hour*60*60)))
print(day, hour, minute)