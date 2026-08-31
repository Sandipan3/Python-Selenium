# A Python set is a mutable collection of unique elements.
print("================= Set ==================")

numbers = {10, 20, 30, 40}
print(numbers)

print("==== Add ====")
numbers.add(50)
print(numbers)

print("==== Duplicate ====")
numbers.add(20)
print(numbers)

print("==== Remove ====")
numbers.remove(30)
print(numbers)

print("==== Discard ====")
numbers.discard(10)
print(numbers)

print("==== Membership ====")
print(20 in numbers)

print("==== Length ====")
print(len(numbers))

# Set operations
print("==== Union ====")
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)
print(a.union(b))

print("==== Intersection ====")
print(a & b)
print(a.intersection(b))

print("==== Difference ====")
print(a - b)
print(a.difference(b))

print("==== Clear ====")
c ={100 , 200 , 300 , 400}
print(c)
c.clear()
print(c)

print("==== Traversal ====")
for num in numbers:
    print(num)

print("==== Traversal with index ====")
for i , num in enumerate(numbers):
    print(i,num) 