from datetime import date
atual = date.today().year
ano = int(input('Qual o ano de nascimento?'))
idade = atual - ano
if idade <= 9:
    print(f'Se você tem {idade} anos, Você esta na categoria MIRIM.')
elif 9 < idade <= 14:
    print(f'Se você tem {idade} anos, Você está na categoria INFANTIL.')
elif 14 < idade <= 19:
    print(f'Se você tem {idade} anos, Você se encontra na categoria JUNIOR.')
elif 19 < idade <= 20:
    print(f'Se você tem {idade} anos, Você se encontra na categoria SÉNIOR.')
else:
    print(f'Se você tem {idade} anos, Você se encontra na categoria MASTER.')

