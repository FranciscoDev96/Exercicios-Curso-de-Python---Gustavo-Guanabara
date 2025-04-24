cont = conth = mulher = 0
while True:
    print('-=' * 20)
    print('-=' * 10, 'CADASTRE UMA PESSOA', '-=' *10)
    print('-=' * 20)
    idade = int(input('Idade:'))
    sexo = str(input('Sexo M/F:')).upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo M/F:')).upper()[0]
    print('-=' * 30)
    loop = str(input('Quer cadastrar mais pessoas? [S/N]')).upper()[0]
    while loop not in 'SN':
        loop = str(input('Quer cadastrar mais pessoas? [S/N]')).upper()[0]
    if idade >= 18:
        conth += 1
    if sexo == 'M':
        cont+=1
    if sexo == 'F' and idade < 20:
        mulher+=1
    if loop == 'N':
         break
print('-=' * 10, 'FINAL DO PROGRAMA', '-=' *10)
print(f'Foram cadastradas \033[32m{conth}\033[m pessoas que possuem 18 anos ou mais.')
print(f'Foram cadastrados \033[32m{cont}\033[m homens.')
print(f'Foram cadastradas \033[32m{mulher}\033[m mulheres com menos de 20 anos.')
