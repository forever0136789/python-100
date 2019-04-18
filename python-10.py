import time
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
time.sleep(1)
print(time.strftime('%y-%m-%d %H:%M:%S',time.localtime(time.time())))
