sentence = "hello my name is Csaba"
x = {char: sentence.count(char) for char in set(sentence)}
print(x)