def day_number():
    global c
    c = 366
    d = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    e = []
    i = 0 
    for x in range(0, c):
        if i == 7:
            i = 0
               
               
        e.append(d[i])
        i += 1
    print(e)
    print(x)
          
day_number()