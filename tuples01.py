# Tuple: ordered, immutable allows duplicate elements
mytuple = ("Csaba",)
print(type(mytuple))                                # return: <class 'tuple'>

mytuple = ("Csaba")
print(type(mytuple))                                # return: <class 'str'>

mytuple = tuple(["Csaba"])
print(type(mytuple))                                # return: <class 'tuple'>

mytuple = ("Csaba", 57, "Eger")
item = mytuple[0]
print(item)

# 19:00