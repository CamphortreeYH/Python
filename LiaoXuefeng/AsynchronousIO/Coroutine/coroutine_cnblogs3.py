def gen():
    for c in "AB":
        yield c
    for i in range(1, 3):
        yield i

print(list(gen()))

def gen2():
    yield from "AB"
    yield from range(1, 3)

print(list(gen2()))