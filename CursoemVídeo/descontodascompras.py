print(10 * '-', 'Loja do Chico', 10 * '-')
valor = float(input('Qual o valor das compras? R$'))
print(''' Como será o pagamento?
[1] A vista no dinheiro ou cheque (10% de desconto)
[2] A vista no cartão (5% de desconto)
[3] 2X no cartão 
[4] 3x no cartão (Juros de 20%)''')
pagamento = int(input('Qual será a opção:'))
if pagamento == 1:
    print(f'Sua compra é de R${valor} e vai custar R${valor - (valor * 0.1):.2f}, com 10% de desconto.')
elif pagamento == 2:
    print(f'Sua compra foi de R${valor}. E vai custar R${valor - (valor * 0.5):.2f}, com 5% de desconto.')
elif pagamento == 3:
    print(f'A sua compra foi de R${valor}. E não terá desconto.')
    print(f'Portanto, será parcelada em 2X de R${valor / 2:.2f} cada parcela.')
elif pagamento == 4:
    total = valor + (valor * 0.2)
    parcelamento = int(input('Em quantas parcelas você gostaria de fazer?'))
    parcelas = total / parcelamento
    print(f'A sua compra foi de R${valor}. E vai sair R${total}, com 20% de juros. Sendo cada parcela o valor de R${parcelas}')
else:
    print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE.')



