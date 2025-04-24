lista_geral = [[], []]
valor = 0
for v in range(0,7):
    valor = int(input(f'Digite o {v+1}º valor:'))
    if valor % 2 == 0:
        lista_geral[0].append(valor)
    else:
        lista_geral[1].append(valor)
lista_geral[0].sort()
lista_geral[1].sort()
print(f'Os números pares digitados, são: {lista_geral[0]}.')
print(f'Os números ímpares digitados, são: {lista_geral[1]}.')


