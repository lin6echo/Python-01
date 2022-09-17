d = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
c = 366
e = []

def day_name():
    i = 0 
    for x in range(0, c):
        if i == 7:
            i = 0
        e.append(d[i])
        i += 1
    print(e)
    
day_name()

def day_number():
    for x in range(1, c):
        print(x)
    
day_number()