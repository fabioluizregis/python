# Tuples - Elementos que não podem ser mudados/alterados

t = ("Norway", 4.953, 7)
print(t)
print(t[0])
print(len(t))

for item in t:
    print(item)

t = t + (2312.0, 265e9)
print(t)
print(type(t))
h = (391)
print(type(h))

def minmax(items):
    return min(items), max(items)

print(minmax([43, 56, 12, 63, 7623, 65, 12346, 23, 2623]))

(a , (b, (c, d))) = (4, (3, (2, 1)))
print(a)
print(b)
print(c)
print(d)


print(tuple("Carmichael"))
