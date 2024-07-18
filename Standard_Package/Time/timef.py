# import time

# def send_email():
#     for i in range(10000000):
#         pass
# #to performance calculation
# print(time.time()) # number of second 1990

# start = time.time()
# send_email()
# end = time.time()
# duration = end - start
# print(duration) #0.1526334285736084


#datatime -=======================================
from datetime import datetime
import time

print(datetime(2019,1,1)) #2019-01-01 00:00:00

print(datetime.now() )  #2024-07-18 11:58:27.512063
#convert str to datetime 
#Y for 4 digit year, %m:2digit month, 
dt = datetime.strptime("2018/01/01","%Y/%m/%d")

#convert timestamp 2 datetime
print(datetime.fromtimestamp(time.time())) #2024-07-18 11:59:56.597316

#convet 2 string
dt = datetime.now()
print(dt.strftime("%Y/%m")) #2024/07

#time detrla ===========================================
from datetime import timedelta

dt1 = datetime(2019,1,1)
dt2 = datetime.now()

dur = dt2-dt1
print(dur) #2026 days, 11:41:42.084468
print(dur.days) #2026 
print(dur.seconds) #44354 = 11:41:42
print(dur.total_seconds()) #175004571.157836

#for next day
dt1 = datetime(2019,1,1) + timedelta(days=1,seconds=1000)
print(dt1)  #2019-01-02 00:00:00

