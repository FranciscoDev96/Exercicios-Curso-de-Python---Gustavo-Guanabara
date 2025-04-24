print('O limite de velocidade é de 80Km/h.')
multa = float(input('Qual era a velocidade em Kilometros por hora:'))
if multa > 80:
    print('Você foi multado!')
    print(f'Você receberá uma cobrança de R$ {(multa - 80) * 7:.2f} reais! \nSendo que é cobrado R$7.00 reais por kilometro ultrapassado')
else:
    print('Você tá safe!')




