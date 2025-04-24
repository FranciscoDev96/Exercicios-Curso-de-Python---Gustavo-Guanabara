pessoas = []
dados = []
maior = 0
menor = 0
while True:
    dados.append(str(input('Digite o nome:')))
    dados.append(float(input('Digite o peso:')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        elif dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('Deseja continuar? [S/N]'))
    if resp in'Nn':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior}. Que foram das pessoas:', end=' ')
for v in pessoas:
    if v[1] == maior:
        print(f'{v[0]}', end=' ')
print(f'\nO menor peso foi de {menor}. Que foram das pessoas:', end=' ')
for v in pessoas:
    if v[1] == menor:
        print(f'{v[0]}', end=' ' )














