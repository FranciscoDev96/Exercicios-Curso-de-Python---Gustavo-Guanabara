import datetime
hoje = datetime.datetime.now()
agora = hoje.year
cont_maioridade = 0
cont_menor = 0
for c in range(1, 8):
    ano = int(input(f'Digite o ano de nascimento da {c}º pessoa:'))
    maioridade = agora - ano
    if maioridade >= 21:
        cont_maioridade += 1
    elif maioridade < 21:
        cont_menor +=1
print(f'{cont_maioridade} pessoas, ALCANÇARAM a maioridade')
print(f'{cont_menor} pessoas, NÃO atingiram a maioridade')




