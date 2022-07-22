words = "Why sometimes I have believed as manu as six impossible things before breakfast"
palavras = words.split()
print(palavras) 
print(len(palavras))

print([len(item) for item in palavras])


# Set Comprehensions
from math import factorial
s = {len(str(factorial(x))) for x in range(20)}
print(type(s))
print(s)