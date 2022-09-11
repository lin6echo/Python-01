# List: ordered, mutable, allows duplicate elements

mylist = ["Ford", "Mercedes", "Toyota"]
print(mylist)

mylist.append("Moszkvics")
print(mylist)

mylist.insert(0, "Lada")
print(mylist)

item = mylist.pop()
print(item)
print(mylist)

mylist = ["Ford", "Mercedes", "Toyota"]
mylist.remove("Ford")
print(mylist)

mylist = ["Ford", "Mercedes", "Toyota"]
mylist.clear()
print(mylist)




