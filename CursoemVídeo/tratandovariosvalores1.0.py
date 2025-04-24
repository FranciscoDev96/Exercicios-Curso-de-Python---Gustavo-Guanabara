num = cont = soma = 0
num = int(input('Digite um número: Para parar digite [999]:'))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um número: Para parar digite [999]:'))
print(f'Você digitou {cont} números, e a somatória dos números digitados foi {soma}.')