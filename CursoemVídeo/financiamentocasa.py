casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Qual o seu salário? R$'))
financiamento = int(input('Em quantos anos você quer pagar?'))
parcela = casa / (financiamento * 12) #valor da parcela
if parcela >= salario * 0.3:
    print(f'Infelizmente, a parcela ficou em: R${parcela:.2f}. Sendo maior que 30% do seu salário. Portanto, o empréstimo foi negado.')
else:
    print(f' A parcela ficou em: R${parcela:.2f}. Parabéns, seu empréstimo foi aprovado.')

