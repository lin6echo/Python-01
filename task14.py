def day_number():
     global c
     c = 365
     d = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
     e = []
     i = 0 
     for x in range(0, c):
          if i == 6: 
               i = 0
               i = i +1
               
          e.append(d[x])
          print(e)
          
day_number()



# def day_name():
#      d = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
#      for x in d:
#           print(x)
     
# day_name()          




