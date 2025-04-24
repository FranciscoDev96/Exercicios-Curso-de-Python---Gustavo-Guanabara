lista = []
for p in range(1, 6):
    peso = float(input(f'Peso da {p}º pessoa:'))
    lista += [peso]
print('O maior peso foi:',max(lista))
print('O menor peso foi:',min(lista))
