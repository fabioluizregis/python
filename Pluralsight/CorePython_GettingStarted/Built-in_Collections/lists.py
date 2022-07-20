r = [1, -4, 10, -16, 15]
print(r[-1]) # ultimo elemento da lista
print(r[len(r) - 1]) # último elemento da lista

print(r[-2]) # penúltimo elemento da lista
print(r[0]) # primeiro elemento da lista


# slicing
s = [3, 186, 4431, 74400, 1048444]
print(s[1:3]) # imprime todos os elementos à partir da posição 1 até a posição (3-1)
print(s[1:-1]) # imprime todos os elementos à partir da posição 1 até a posição (-1-1)
print(s[2:]) # imprime todos os elementos à partir da posição 2
print(s[:2]) # imprime todos os elemento até a posição (2-1)

print(s[:]) # imprime toda a lista

t = s # copia a lista apontando para a mesma posição de memória
print(t is s)

r = s[:] # copia a lista, criando uma nova posicao de memória para r (é uma nova lista igual a anterior)
print(r is s)
print(r[:])
print(s[:])

print(s.index(4431)) # em qual posicao está o elemento 4431?

u = "jackdaws love my big sphinx of quartz".split()
print(u)
del u[3]
print(u)
u.remove('jackdaws')
print(u)


a = 'I accidentally the whole universe'.split()
print(a)
a.insert(2, "destroyed")
print(a)

g = [1, 11, 21]
g.reverse()
print(g)

h = [17, 41, 29]
h.sort()
print(h)
h.sort(reverse=True)
print(h)