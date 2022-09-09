import calendar
import datetime
from sqlite3 import Timestamp
import pandas as pd


# x_date = datetime.date(2022, 1, 22)
# no = x_date.weekday()

# if no < 5:
#     print("Date is Weekday")
# else:  # 5 Sat, 6 Sun
#     print("Date is Weekend")

# d = date.today()
# print('Date is:', d)
# x = calendar.day_name()
# print(x)

# January = list(range(1,32))
# February = list(range(1,29))
# March = list(range(1,32))
# April = list(range(1,31))
# May = list(range(1,32))
# June = list(range(1,31))
# July = list(range(1,32))
# August = list(range(1,32))
# September = list(range(1,31))
# October = list(range(1,32))
# November = list(range(1,31))
# December = list(range(1,32))

# x = January + February + March + April + May + June + July + August + September + October + November + December
# print(len(x))



# # get current datetime
# dt = 2020-06-06
# print('Datetime is:', dt)

# # get weekday name
# print('day Name:', dt.strftime('%A'))
d = Timestamp(2022,1,1)

#d = pd.Timestamp('2022-05-02')
#print(d.dayofweek, d.day_name())

# weekday (Monday =0 Sunday=6)
print('Weekday Number:', d.weekday())

# isoweekday(Monday =1 Sunday=6)
print('ISO Weekday Number:', d.isoweekday())

# get weekday name
print('Weekday Name:', d.strftime('%A'))

# get day name
x = calendar.day_name[d.weekday()]
print('Weekday name is:', x)
