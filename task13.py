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
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for x in weekdays:
    print(x)

numbers = year
for numbers in year:
    
    print(numbers)
    
    my_list = [10, 20, 30, 40]

for index, val in enumerate(my_list, start=1):
    print(index, val)
    
