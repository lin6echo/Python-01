def day_name():
    global c
    c = 366
    global d
    d = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    e = []
    i = 0 
    for x in range(0, c):
        if i == 7:
            i = 0
        e.append(d[i])
        i += 1
    print(e)
    
          
day_name()

def day_number():
    for x in range(0, c):
        print(x)
    
          
day_number()