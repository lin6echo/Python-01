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

year = tuple(January + February + March + April + May + June + July + August + September + October + November + December)
weekday = "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"

keys = [year]
values = [weekday]
dictionary = dict(zip(keys, values))
print(dictionary) # {'a': 1, 'b': 2, 'c': 3}
