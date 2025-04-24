salario = float(input('Digite seu salário para ver o seu aumento: R$'))
if salario >1250.00:
    aumento = 0.10 * salario + salario
    print(f' O seu novo salário será de R${aumento:.2f}')
if salario <=1250.00:
    aumento = 0.15 * salario + salario
    print(f' O seu novo salário é de R$ {aumento:.2f}')




