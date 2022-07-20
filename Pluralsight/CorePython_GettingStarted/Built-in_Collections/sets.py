from importlib.metadata import packages_distributions


p = {6 ,28, 496, 8128, 33550336}
print(p)
print(type(p))

d = {}  #criating an empty dictionary
print(type(d))

e = set()
print(e)

s = set([2, 4, 16, 64, 4096, 65536, 262144])
print(s)

t = [1, 4, 2, 1, 7, 9, 9]
print(set(t))

for x in {1, 2, 4, 8, 16, 32}:
    print(x)

q = {2, 9, 6, 4}
print(3 in q)
print(3 not in q)

k = {81, 108}
print(k)

k.add(54)
print(k)

k.add(12)
print(k)

k.update([37, 128, 97])
print(k)

k.remove(97)
print(k)

j = k.copy()
print(j)

m = set(j)
print(m)
print("\n")
blue_eyes = {'Olivia', 'Harry', 'Lily', 'Jack', 'Amelia'}
blond_hair = {'Harry', 'Jack', 'Amelia', 'Mia', 'Joshua'}
smell_hcn = {'Harry', 'Amelia'}
taste_ptc = {'Harry', 'Lily', 'Amelia', 'Lola'}
o_blood = {'Mia', 'Joshua', 'Lily', 'Olivia'}
b_blood = {'Amelia', 'Jack'}
a_blood = {'Harry'}
ab_blood = {'Joshua', 'Lola'}

print(blue_eyes.union(blond_hair))
print(blue_eyes.union(blond_hair) == blond_hair.union(blue_eyes))

print("\n")
print(blue_eyes.intersection(blond_hair))
print(blue_eyes.intersection(blond_hair) == blond_hair.intersection(blue_eyes))

print("\n")
print(blond_hair.difference(blue_eyes))
print(blond_hair.difference(blue_eyes) == blue_eyes.difference(blond_hair))

print("\n")
print(blond_hair.symmetric_difference(blue_eyes))
print(blond_hair.symmetric_difference(blue_eyes) == blue_eyes.symmetric_difference(blond_hair))

print("\n")
print(smell_hcn.issubset(blond_hair))

print("\n")
print(taste_ptc.issuperset(smell_hcn))

print("\n")
print(a_blood.isdisjoint(o_blood)) #We must have A blood type OR B blood type.. never both