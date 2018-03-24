vals = []

for x in range(10):
    if x % 2 != 0:
        vals.append(x * x)

for val in vals:
    print(val)

print()

# list comprehension
vals = [x * x for x in range(10) if x % 2 != 0]

for val in vals:
    print(val)
