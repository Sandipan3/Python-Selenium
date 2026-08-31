# range generates a sequence of numbers.
print("================= Range ==================")

print("==== Basic ====")
r = range(5)

for x in r:
    print(x)

print("==== (Start , Stop) ====")
for x in range(2, 6):
    print(x)

print("==== (Start , Stop , Step) ====")
for x in range(0, 10, 2):
    print(x)