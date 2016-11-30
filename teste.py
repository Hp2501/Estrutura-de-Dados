string = 'abcdef'
listaString = list(string)
string2 = 'fedcba'
for i in range(0, len(string) - 1):
    listaString.pop(0)
    listaString.insert(len(string2), string2[i])

novaString = "".join(listaString)

print(listaString)
print(novaString)