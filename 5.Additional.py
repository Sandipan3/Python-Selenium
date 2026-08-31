# Generators: Generators produce values lazily.
def numbers():
    yield 1
    yield 2
    yield 3

for x in numbers():
    print(x)

# yield: pauses the function and remembers its state.