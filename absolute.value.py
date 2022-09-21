class ImplementAbs:
    def __init__(self, string):
        self.string = string
        
    def __abs__(self):
        return self.string.lower()
    
costum_obj = ImplementAbs("HELLO")

x = abs(-9)
y = abs(-100.234)
z = abs(costum_obj)

print(x)
print(y)
print(z)