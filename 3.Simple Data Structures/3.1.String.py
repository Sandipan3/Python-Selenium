# A Python string is an immutable sequence of characters.
print("=================String==================")
s = "hello"
print(s)

print("====indexing====")
print(s[0])
print(s[1])
print(s[-1])
print(s[-2])

print("====slicing====")
print(s[1:4:2])
print(s[::-1])

print("==== concatenate ====")
s = "H" + s[1:]
print(s)

print("====Upper====")
print(s.upper())

print("====Lower====")
print(s.lower())

print("====Strip====")
s = "     hello     "
print(".",s,".")
print(".",s.strip(),".")

print("==== Replace ====")
s = "hello world"
print(s.replace("world","python"))

print("==== Split ====")
s = "apple,banana,orange"
print(s.split(","))

print("==== Find ====")
s = "hello world"
print(s.find("world"))

print("==== Length ====")
print(len(s))

print("==== Membership ====")
print("hello" in s)
print("xyz" not in s)

print("==== Traversal ====")
for ch in s:
    print(ch)

print("==== Traversal with index ====")
for i in range(len(s)):
    print(i,s[i])