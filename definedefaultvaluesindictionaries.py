# Define default values in Dictionaries with .get() and .setdefault()

my_dict = {"item": "football", "price": 10.00}
count = my_dict.get("count", 0)
print(count)

count = my_dict.setdefault("count", 0)
print(count)
print(my_dict)