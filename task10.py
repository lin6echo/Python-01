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

year = January + February + March + April + May + June + July + August + September + October + November + December
weekday = "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"

éves_napok_nevei = []

for x in year:
     éves_napok_nevei.append(list(weekday))
print(éves_napok_nevei)
print(len(éves_napok_nevei))

éves_napok_számai = []

for x in year:
    éves_napok_számai = year
print(éves_napok_számai)
print(len(éves_napok_számai))


# List1 = year
# List2 = éves_napok_nevei


# d = {List1[n]: List2[n] for n in range(List1)}
# print(d)