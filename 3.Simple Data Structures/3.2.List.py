# A Python list is a mutable, ordered collection of elements.
print("================= List ==================")

numbers = [10, 20, 30, 40, 50]
print(numbers)

print("==== indexing ====")
print(numbers[0])
print(numbers[-1])

print("==== slicing ====")
print(numbers[1:4])
print(numbers[::-1])

print("==== Change value ====")
numbers[0] = 100
print(numbers)

print("==== Append ====")
numbers.append(60)
print(numbers)
a = [60 , 70]
numbers.append(a)
print(numbers)

print("==== Extend ====")
b = [70 , 80]
numbers.extend(b)
print(numbers)

print("==== Insert ====")
numbers.insert(1, 15)
print(numbers)

print("==== Remove ====")
numbers.remove(30)
print(numbers)

print("==== Pop ====")
x = numbers.pop()
print(x)
print(numbers)

print("==== Length ====")
print(len(numbers))

print("==== Sort ====")
c = [15 ,35 ,25 , 5]
c.sort()
# c.sort(reverse=True)
print(c)

print("==== Reverse ====")
numbers.reverse()
print(numbers)

print("==== Clear ====")
c.clear()
print(c)

print("==== Traversal ====")
for num in numbers:
    print(num)

print("==== Traversal with index ====")
for i in range(len(numbers)):
    print(i,numbers[i])