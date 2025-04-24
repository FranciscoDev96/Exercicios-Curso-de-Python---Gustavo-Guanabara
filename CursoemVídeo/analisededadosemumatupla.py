numeros = (int(input('Digite um número:')),
            int(input('Digite um número:')),
           int(input('Digite um número:')),
            int(input('Digite um número:')))
print(f'Você digitou os seguintes valores: {numeros}.')
print(f'O número 9 foi digitado {numeros.count(9)} vezes.')
if 3 in numeros:
    print(f'O valor 3 aparece primeiro na {numeros.index(3) + 1}ª posição.')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição.')
print('Os números pares digitados foram:', end=' ')
for c in numeros:
    if c % 2 ==0:
        print(f'{c}', end=' ')


