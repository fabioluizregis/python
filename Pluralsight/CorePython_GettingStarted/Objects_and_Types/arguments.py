m = [9, 15, 24]

def modify(k):
    k.append(39)
    print("k = ", k)

modify(m)

print("m = ", m)


print("\n####################################################\n")

f = [14, 23, 37]
def replace(g):
    g = [17, 28, 45]
    print("g = ", g)

replace(f)
print("f = ", f)

print("\n####################################################\n")

def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)

banner("This is a banner")

banner("Sun, Moon and Stars", "*")
