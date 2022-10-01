# Merge two dictionaries

d1 = {"name": "Alex", "age": 25}
d2 = {"name": "Alex", "city": "New York"}
merged_dict = {**d1, **d2}
print(merged_dict)