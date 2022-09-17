c = 366
d = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
e = []

def yearly_days_name():
    i = 0
    for x in range(1, c):
        if i == 7:
            i = 0
        e.append(d[i])

        i += 1
    print(e)
    

yearly_days_name()

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

January = 32

e =[]

i = 0
for x in range(1, January):
    if i == 7:
       i = 0

    e.append(d[i])
    i += 1


    print(e)
    