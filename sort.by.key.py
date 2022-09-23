from ast import Lambda


lst = [[1, 2], [3, 4], [4, 2], [-1, 3], [4, 5], [2, 3]]

lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)

lst.sort(key=lambda x: x[1])
print(lst)

lst.sort(key=lambda x: x[1] + x[0])
print(lst)

def sort_func(x):
    return x[1] + x[0]

lst.sort(key=sort_func)
print(lst)

sorted(lst, key=sort_func)
print(lst)




