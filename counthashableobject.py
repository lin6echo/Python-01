# Count hashable objects with collections.Counter

from collections import Counter

my_list = [10,10,10,5,5,2,9,9,9,9,9,9]
counter = Counter(my_list)

print(counter)
most_common = counter.most_common(2)
print(most_common)