print('Parabéns!! Você acaba de ganhar 5% de desconto em toda a nossa loja! Digite o preço abaixo para descobrir quanto terá de desconto:')
n1 = float(input('Digite o valor da sua compra: R$'))
n2 = n1 - (n1 / 100 * 5)
print(f'A sua compra com 5% de desconto, vai sair: R${n2:.2f}')

