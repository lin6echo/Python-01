tup = (1, 2, 3, 4, 5)
lst = [1, 2, 3, 4, 5]
string = "hello"
dic = {'a': 1, 'b': 2}
coords = [4, 5]

a, b, c, d, e = tup
print(a,b,c,d,e)

a, b, c, d, e = lst
print(a,b,c,d,e)

a, b, c, d, e = string
print(a,b,c,d,e)

a,b = dic
print(a,b)

a,b = dic.values()
print(a,b)

a,b = dic.items()
print(a,b)

x, y = coords
print(x,y)