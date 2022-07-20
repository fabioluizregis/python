urls = { 'Google' : 'http://google.com',
         'Pluralsight' : 'http://pluralsight.com',
         'Sixty North' : 'http://sixty-north.com',
         'Microsoft' : 'http://microsoft.com'}

print(urls['Pluralsight'])

names_and_ages = [('Alice', 32), ('Bob',48), ('Charlie', 28), ('Daniel', 3)]
d = dict(names_and_ages)
print(d)
other_names_and_ages = [('Fulano', 22), ('Ciclano', 53)]
e = dict(other_names_and_ages)
print(e)

d.update(e) #adiciona o dicionário 'e' em 'd'
print(d)

for names in d:
    print(f"{names} => {d[names]}")