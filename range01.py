# Syntax: range(start, stop, step)

# Parameter:

# start: integer starting from which the sequence of integers is to be returned
# stop: integer before which the sequence of integers is to be returned. The range of integers ends at stop – 1.
# step: integer value which determines the increment between each integer in the sequence

# printing a number
for i in range(0,10,2):
    print(i, end=" ")
print()
  
from itertools import chain
 
# Using chain method
print("Concatenating the result")
res = chain(range(15), range(10, 20, 2))
 
for i in res:
    print(i, end=" ")
    
# Accessing range() with an index value
ele = range(10)[0]
print("First element:", ele)
 
ele = range(10)[-1]
print("\nLast element:", ele)
 
ele = range(10)[4]
print("\nFifth element:", ele)

# iterate the loop 5 times
for i in range(5):
    print(i, 'Hello')



