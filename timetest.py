from datetime import datetime
from datetime import date

today = date.today()
print(today)
print(type(str(today)))

now = datetime.now()

current_time = now.strftime("%H:%M:%S")

query_time =  str(today) +" " +current_time
print (current_time)
print( type(current_time))


id = str(130)
print(id[1:])
# print(query_time)
# print(len(query_time))
# print(query_time[0:17])
# query_time = query_time[0:17] + '10'
# print(query_time)