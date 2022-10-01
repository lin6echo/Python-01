# Use List Comprehensions Instead of for raw loops

squares = []
for i in range(10):
    squares.append(i*i)

print(squares)

squares = [i*i for i in range(10)]
print(squares)