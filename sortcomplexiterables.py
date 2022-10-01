# Sort complex iterables with sorted()

data = [3, 5, 1, 10, 9]
sorted_data = sorted(data)

print(sorted_data)

data = [{"name": "Max", "age": 6},
        {"name": "Lisa", "age": 20},
        {"name": "Ben", "age": 9}]

sorted_data = sorted(data, key=lambda x: x["age"])
print(sorted_data)