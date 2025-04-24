soma = 0
homens = []
for id in range(1, 5):
    nome = str(input(f'Digite o nome da {id}º pessoa:')).strip()
    sexo = str(input(f'Digite o sexo da {id}º pessoa [M/F]:')).upper().strip()
    idade = int(input(f'Digite a idade da {id}º pessoa:'))
    print(20 * '-=')
    soma += idade
    media = soma / 4
    if sexo == 'M':
        homens = homens +[nome]


print(f'A média das idades digitadas foi de {media:.1f} anos.')

