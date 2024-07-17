import datetime
#date now
x = datetime.datetime.now()
print(x)
print('year:',x.year,x.month, x.day)  #2024 7 11

#microsecond
print(x.strftime('f'))  #545138

#second
print(x.strftime('%S')) #09

#minutes
print(x.strftime('%M'))  #45

#hour
print(x.strftime('%H'))  #17 (24hours)
print('==>',x.strftime('%I')) # 05 
print('==>',x.strftime('%p')) # am

#day
print(x.strftime("%A"))  #Thursday
print(x.strftime("%a"))  #Thu (short name)
print(x.strftime("%d"))  #day of month 11

#week
print(x.strftime("%w"))  #0 is Sunday ,1 is monday ,...

#month
print(x.strftime("%B"))  #July
print(x.strftime("%b"))  #Jul(short name)
print(x.strftime("%m"))  #07 (month as number)

#year
print(x.strftime("%y"))  #24(without century)
print(x.strftime("%Y"))  #2024
print(x.strftime("%j"))  #year number 34
print(x.strftime("%U"))  #weak number of year (0--53)


#other format -------------------------------------------
print('==>',x.strftime("%z"))  #UTC offset
print('==>',x.strftime("%Z"))  #timezone
print('==>',x.strftime("%c"))  #Thu Jul 11 11:08:06 2024
print('==>',x.strftime("%C"))  #20 Century
print('==>',x.strftime("%x"))  #07/11/24
print('==>',x.strftime("%G"))  #2024











#date specefic time
x = datetime.datetime(2020,1,1)
