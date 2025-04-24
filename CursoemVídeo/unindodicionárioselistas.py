dados = dict()
grupo = list()
mulheres = list()
acima_media = list()
anos = list()
cont = soma = media = 0
while True:
    dados['Nome'] = str(input('Nome:'))
    dados['Idade'] = int(input('Idade:'))
    anos.append(dados['Idade'])
    while True:
        dados['Sexo'] = str(input('Sexo:'))
        if dados['Sexo'] in 'MmFf':
            break
        else:
            print('ERRO! Por favor,digite apenas M ou F.')
    grupo.append(dados.copy())
    cont+= 1
    soma += dados['Idade']
    media = soma / cont
    if dados['Sexo'] in 'Ff':
        mulheres.append(dados['Nome'])
    while True:
        resp = str(input('Deseja continuar? [S/N]:'))
        if resp in 'SsNn':
            break
        else:
            print('ERRO! Por favor,digite apenas S ou N.')
    if resp in 'Nn':
        break
print(f' -Foram cadastradas {cont} pessoas no sistema.')
print(f' -A média de idade é de {media:.1f} anos.')
print(' -As mulheres cadastradas foram', end=' ')
for c in mulheres:
   print(f'{c}',end=' ')
print('\nLista das pessoas que estão acima da média:')
for p in grupo:
    if p['Idade'] > media:
        print(f'{p}')
        print()


