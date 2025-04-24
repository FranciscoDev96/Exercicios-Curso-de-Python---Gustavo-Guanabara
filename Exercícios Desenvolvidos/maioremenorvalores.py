resp = 'S'
soma = cont = maior = menor = 0
while resp == 'S':
    num = int(input('Digite um número:'))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N:')).strip().upper()
media = soma / cont
print(f'Você digitou {cont} números e a média dos números foi de {media:.2f}.')
print(f'O maior número foi {maior} e o menor número foi {menor}.')

