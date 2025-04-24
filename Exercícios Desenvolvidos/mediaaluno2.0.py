nota1 = float(input('Digite a primeira nota:'))
nota2 = float(input('Digite a segunda nota:'))
media = (nota1 + nota2) / 2
if media < 5.0:
    print(f'Sua média foi de {media}. Como foi abaixo de 5.0, você está REPROVADO.')
elif 5 <= media < 6.9:
    print(f'Sua média foi de {media}. Como sua nota está entre 5.0 e 6.9, você está de RECUPERAÇÃO.')
else:
    print(f'Sua média foi de {media}. Você foi APROVADO. \nParabéns!!!')

