January = list(range(1,32))
February = list(range(1,29))
March = list(range(1,32))
April = list(range(1,31))
May = list(range(1,32))
June = list(range(1,31))
July = list(range(1,32))
August = list(range(1,32)) 
September = list(range(1,31))
October = list(range(1,32))
November = list(range(1,31))
December = list(range(1,32))

n = January + February + March + April + May + June + July + August + September + October + November + December



c = 366

for x in range(1, c):
     print(x)

DAYS = 'Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday', 'Saturday', 'Sunday'


d = []

for x in n:
     d.append(list(DAYS))
print(d)

# for x in year:
#      éves_napok_nevei.append(list(weekday))
# print(éves_napok_nevei)