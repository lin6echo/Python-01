week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

d1 = dict()
i = 0
for x in range(1,32):
    if i == 7:
        i = 0
    d1[x]= week[i]
    i += 1
print(d1)






