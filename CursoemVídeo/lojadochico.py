print( '=' * 10, 'LOJA DO CHICO', '=' * 10)
soma = contm = cont = menor = 0
barato = ' '
while True:
    produto = str(input('Qual o produto:'))
    preco = float(input('Qual o valor? R$'))
    soma += preco
    cont += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    if preco > 1000:
        contm += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]:')).upper().strip()[0]
    if resp == 'N':
        break
    print('-' * 30)
print('-' * 30)
print(f'O valor total da compra foi de R${soma:.2f}')
print(f'{contm} produtos custaram mais de R$1000.00,')
print(f'O produto de menor valor foi {barato} de R${menor:.2f}')




