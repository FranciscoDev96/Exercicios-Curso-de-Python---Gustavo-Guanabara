print('='*30)
print ('BANCO DO CHICO')
print('='*30)
saque = int(input('Qual o valor será sacado?: R$'))
nota50 = saque % 50
valor50 = saque // 50
nota20 = nota50 % 20
valor20 = nota50 // 20
nota10 = nota20 % 10
valor10 = nota20 // 10
nota1 = nota10 % 1
valor1 = nota10 // 1
if valor50 > 0:
    print(f'Total de {valor50} cédulas de R$50.00')
if valor20 > 0:
    print(f'Total de {valor20} cédulas de R$20.00')
if valor10 > 0:
    print(f'Total de {valor10} cédulas de R$10.00')
if valor1 > 0:
    print(f'Total de {valor1} cédulas de R$1.00')
print('='*30)
print('Obrigado por utilizar nosso banco! Volte sempre!')
