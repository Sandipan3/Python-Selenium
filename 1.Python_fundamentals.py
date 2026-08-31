# data types
# use type(x) to see the data type
print("===============DATA TYPES============")
a = 10
print(f"The data type of {a} is: {type(a)}")

b = 10.5
print(f"The data type of {b} is: {type(b)}")

c = "hello"
print(f"The data type of {c} is: {type(c)}")

d = True
print(f"The data type of {d} is: {type(d)}")

e = None
print(f"The data type of {e} is: {type(e)}")

f = [1,2,3]
print(f"The data type of {f} is: {type(f)}")

g = (1,2,3)
print(f"The data type of {g} is: {type(g)}")

h = {1,2,3}
print(f"The data type of {h} is: {type(h)}")

i = {"a" : 1} 
print(f"The data type of {i} is: {type(i)}")


# input: use input() -> always string
print("===============Input============")
name = input("Enter a string")
print(name)

# convert it to number
x = int(input("Enter a number"))
print(x)

# multiple inputs
a, b = map(int, input("Enter two numbers").split())
print(a , b)

# array input
arr = list(map(int , input("Enter three numbers").split()))
print(arr)

print("===============Operators============")

print("==Aritmetic==")
print(f"The value of 7 + 2  is: {7+2}")
print(f"The value of 7 - 2  is: {7-2}")
print(f"The value of 7 * 2  is: {7*2}")
print(f"The value of 7 / 2  is: {7/2}")
print(f"The value of 7 // 2  is: {7//2}")
print(f"The value of 7 % 2  is: {7%2}")
print(f"The value of 7 ** 2  is: {7**2}")

print("==Comparison==")
print(f"The value of 7 > 2  is: {7>2}")
print(f"The value of 7 < 2  is: {7<2}")
print(f"The value of 7 >= 2  is: {7>=2}")
print(f"The value of 7 <= 2  is: {7<=2}")
print(f"The value of 7 == 2  is: {7==2}")
print(f"The value of 7 != 2  is: {7!=2}")

print("==Logical==")
print(f"The value of 7 and 2  is: {7 and 2}")
print(f"The value of 7 or 2  is: {7 or 2}")
print(f"The value of !7  is: !{7}")

print("==Ternary==")
x = 5
result = "even" if(x%2==0) else "odd"
print(result)


print("===============Conditional statements============")
x = 10
if(x > 0):
    print("positive")
elif(x < 0):
    print("negative")
else:
    print("zero")


print("===============Loops============")
print("==For==")
for x in range(10):
    print(x)


print("==while==")
x = 0
while x<10 :
    print(x)
    x += 1

print("==array traverse==")
arr = [10, 20, 30]
for i in range(len(arr)):
    print(f"The element at index {i} is {arr[i]}")
