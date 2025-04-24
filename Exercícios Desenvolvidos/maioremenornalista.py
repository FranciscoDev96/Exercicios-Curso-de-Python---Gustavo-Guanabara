valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor:')))
for c, v in enumerate(valores):
    print(f'O maior valor é {max(valores)} e esta na posição {c}.\n O menor valor é {min(valores)} e esta na posição {c}')
print(max(valores))
print(min(valores))





