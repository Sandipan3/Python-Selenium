# A Python tuple is an immutable, ordered collection of elements.
print("================= Tuple ==================")

numbers = (10, 20, 30, 40, 50)
print(numbers)

# numbers[0] = 100 can not do because tuples are immutable.

print("==== indexing ====")
print(numbers[0])
print(numbers[-1])

print("==== slicing ====")
print(numbers[1:4])
print(numbers[::-1])

print("==== Length ====")
print(len(numbers))

print("==== Count ====")
numbers = (10, 20, 20, 30, 20)
print(numbers.count(20))

print("==== Index ====")
print(numbers.index(30))

print("==== Membership ====")
print(20 in numbers)

print("==== Unpacking ====")
a, b, c = (10, 20, 30)
print(a)
print(b)
print(c)

print("==== Traversal ====")
for num in numbers:
    print(num)

print("==== Traversal with index ====")
for i in range(len(numbers)):
    print(i,numbers[i])
