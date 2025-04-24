lista = []
for c in range(0,5):
    lista.append(int(input('Digite um valor:')))
print(lista)
print(max(lista))
print(lista.index(max(lista)))
print(min(lista))
print(lista.index(min(lista))+1)
