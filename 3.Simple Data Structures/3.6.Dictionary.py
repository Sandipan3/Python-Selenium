# A Python dictionary stores data as key-value pairs.
print("================= Dictionary ==================")

student = {
    "name": "John",
    "age": 20,
    "city": "Kolkata"
}

print(student)

print("==== Access value ====")
print(student["name"])
print(student["age"])

print("==== get ====")
print(student.get("name"))
print(student.get("phone"))

print("==== Change value ====")
student["age"] = 21
print(student)

print("==== Add value ====")
student["course"] = "Python"
print(student)

print("==== Remove ====")
student.pop("city")
print(student)

print("==== Keys ====")
print(student.keys())

print("==== Values ====")
print(student.values())

print("==== Items ====")
print(student.items())

print("==== Membership ====")
print("name" in student)

print("==== Length ====")
print(len(student))

print("==== Loop ====")
for key, value in student.items():
    print(key, value)

print("==== Clear ====")
demo = {
    "key1" : "value1",
    "key2" : "value2",
    "key3" : "value3",
    "key4" : "value4",
}
print(demo)
demo.clear()
print(demo)

print("==== Freq Map ====")

print("Numbers:=")
numbers = [1, 2, 2, 3, 3, 3]
print(numbers)
freq  ={}
for num in numbers:
    freq [num] = freq .get(num , 0) + 1
print(freq)


print("Characters:=")
s = "hello"
freq={}
for ch in s:
    freq[ch] = freq.get(ch , 0) + 1
print(freq)

print("Characters:=")
s = "hello world hello python world"
freq = {}
for word in s.split():
    freq[word] = freq.get(word, 0) + 1
print(freq)
