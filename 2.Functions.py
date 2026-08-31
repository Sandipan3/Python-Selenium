print("=================Functions=================")
def add(a,b):
    return a+b

print(add(2,3))

print("======Default Value======")
def divide(a,b=1):
    return (a/b)

print(divide(3))

print("======*args======")
# *args is a tuple
# *args is used when you don't know how many positional arguments you'll receive.

def printItemsArgs(*args):
    for i in args:
        print(i)

printItemsArgs(1, 2, 3, 4)

print("======**kwargs======")
# **kwargs is a dictionary
# **kwargs is used for variable number of keyword arguments.
def printItemsKwargs(**kwargs):
    print(kwargs)

printItemsKwargs(name="Sandipan", age=23, city="Kolkata")

print("======Lambdas======")
# A lambda is a short, anonymous function.

# normal function
def product(a,b):
    return a*b
print(product(2,3))

# lambda expression
# lambda arguments: expression

productLambda = lambda x,y : x*y
print(productLambda(2,3))

""" 
HOF in Python
HOF = Higher-Order Function.

A function is a Higher-Order Function if it does at least one of these:

Takes another function as an argument.
Returns a function. 

SOME HOF:
map(function, iterable)
filter(function, iterable)
sorted(iterable, key=function)
reduce(function, iterable)
"""

numbers = [1,2,3,4,5]
res = list(map(lambda x : x*2 , numbers))
print(res)

res = list(filter(lambda x : x %2 == 0,numbers))
print(res)