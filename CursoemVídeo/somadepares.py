soma = 0
cont = 0
for pergunta in range (1, 7):
    num = int(input(f'Digite o {pergunta}º número:'))
    if num % 2 == 0:
        soma += num
        cont += + 1
print(f'Você me deu {cont} valores em pares.', end=' ')
print(f'A soma dos números pares digitados foi de {soma}.')


