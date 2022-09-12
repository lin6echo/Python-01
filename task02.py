DAYS = 'Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday', 'Saturday', 'Sunday'
MONTHS = 'January', 'February', 'March', 'April', 'May', 'June', 'July','August', 'September', 'October', 'November', 'December'

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

hónap_napjai_számmal = January + February + March + April + May + June + July + August + September + October + November + December
print(len(hónap_napjai_számmal))
print(type(hónap_napjai_számmal))
#print(hónap_napjai_számmal)


#print(January)

éves_napok_nevei = []

for x in hónap_napjai_számmal:
     éves_napok_nevei.append(list(DAYS))
    
#print(YEAR)
print(len(éves_napok_nevei))







    






    


    
    
