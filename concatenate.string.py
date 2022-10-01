# Concat string with .join()

list_of_strings = ["Hello", "my", "friend"]

# BAD WAY

my_string = ""
for i in list_of_strings:
    my_string += i + ""
print(my_string)

# GOOD WAY

my_string = " ".join(list_of_strings)
print(my_string)