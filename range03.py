listType = ['US', 'UK', 'India', 'China']
for i in range(len(listType)):
    print(listType[i])
#------------------------------------------------------
print(list(range(0, 10, 2)))
print(set(range(0, 10, 2))) 
print(tuple(range(0, 10, 2))) 
#--------------------------------------------------------
A = range(0,100)[29]
print(A)
#------------------------------------------------------
r = range(3,8,2) # create range
print(r)

print(type(r)) # get type

list(r) # convert to list
print(list)

it = iter(r) # get iterator 
print(next(it)) # get next 
print(next(it)) # get next
