def day_number():
     global c
     c = 365
     d = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
     e = []
     i = 0 
     for x in range(0, c):
          if i == 6: 
               i = 0
               
          e.append(d[x])
          print(e)
          
day_number()