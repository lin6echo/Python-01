# iterate with enumerate() instead of range(len())

data = [1, 2, -4, -3]
for i in range(len(data)):
    if data[i] < 0:
        data[i] = 0

print(data)

data = [1, 2, -4, -3]
for idx, num in enumerate(data):
    if num < 0:
        data[idx] = 0

print(data)

