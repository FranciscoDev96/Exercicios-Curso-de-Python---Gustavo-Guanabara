numeros = []
while True:
    n = int(input('Digite um número:'))
    if n not in numeros:
        numeros.append(n)
        print('Número adicionado.')
    else:
        print('Número duplicado. Não adicionado.')
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
numeros.sort()
print(f'Os números digitados na ordem crescente foram: {numeros}')



