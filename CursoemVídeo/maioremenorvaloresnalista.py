listanum = []
mai = 0
men = 0
cont = 0
for c in range(0,5):
    listanum.append(int(input(f'Digite um valor para a posição {c}:')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print(f'Você digitou os números: {listanum}')
print(f'O maior valor foi {mai}. Nas posições', end='')
for c, v in enumerate(listanum):
    if v == mai:
        print(f' {c}...', end='')
print(f'\nO menor valor digitado foi {men}. Nas posições', end='')
for c, v in enumerate(listanum):
    if v == men:
        print(f' {c}...', end='')


