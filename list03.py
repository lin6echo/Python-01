mylist = ["Ford", "Mercedes", "Toyota"]
print(mylist)

for i in mylist:
    print(i)
    
if "Ford" in mylist:
    print("Yes")
else:
    print("No")
    
print(len(mylist))

mylist.reverse()
print(mylist)

mylist.sort()
print(mylist)

mylist1 = [1, -5, -1, 3, 9, 4, 2]
new_list = sorted(mylist1)
print(new_list)