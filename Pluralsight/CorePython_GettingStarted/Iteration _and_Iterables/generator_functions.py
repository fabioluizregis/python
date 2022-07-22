def gen123():
    yield 1
    yield 2
    yield 3

g = gen123()
print(g)
print(next(g))
print(next(g))
print(next(g))
# print(next(g))  # Here we hit the limit

for v in gen123():
    print(v)


h = gen123()
i = gen123()

print(h is i)
print(next(h))
print(next(h))
print(next(i))


def gen246():
    print("About to yield 2")
    yield 2
    print("About to yield 4")
    yield 4
    print("About to yield 6")
    yield 6
    print("About to return")

g = gen246()
print(next(g))
print(next(g))
print(next(g))
print(next(g)) # reached the end