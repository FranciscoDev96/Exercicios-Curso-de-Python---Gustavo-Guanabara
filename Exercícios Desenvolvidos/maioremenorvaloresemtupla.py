from random import randint
numeros = randint(1, 10), randint(1, 10), randint(1,
                10), randint(1, 10), randint(1, 10)
print(f'Os valores sorteados foram:', end=' ')
for n in numeros:
    print(f' {n}', end=' ')
maior = max(numeros)
menor = min(numeros)
print(f'\nO maior valor sorteado foi {maior}.\nO menor valor sorteado foi {menor}.')

