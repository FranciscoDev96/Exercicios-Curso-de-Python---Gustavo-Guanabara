sexo = 0
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite seu sexo [M/F]:')).upper().strip()
    if sexo == 'M':
        print('Você se classificou como Masculino')
    if sexo == 'F':
        print(f'Você se classificou como Feminino.')
    if sexo != 'M' and sexo != 'F':
        print('OPÇÃO INVALIDA')
print('Obrigado')





