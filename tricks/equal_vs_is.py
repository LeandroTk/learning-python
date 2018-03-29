a = [1, 2, 3]
b = a
print(a == b)
print(a is b)

c = list(a)

# == evaluates to true if the objects referred by the variables are equal
print(a == c)
# is evaluates to true if both variables point to the same object
print(a is c)
