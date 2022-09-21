x = []

for i in range(100):
    x.append(0)
    
print(x)

x = [0 for i in range(100)]
print(x)

x = [i for i in range(100)]
print(x)

x = [i for i in range(100) if i % 2 == 0]
print(x)

x = [i for i in "hello"]
print(x)