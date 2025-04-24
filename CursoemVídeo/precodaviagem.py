dist = float(input('Qual será a distância da sua viagem?'))
if dist <= 200:
    valor = dist * 0.50
    print(f'A passagem será de: R$ {valor:.2f}')
else:
    print('Você ganhou um desconto')
    valord = dist * 0.45
    print(f'A passagem será de: R$ {valord:.2f}')

