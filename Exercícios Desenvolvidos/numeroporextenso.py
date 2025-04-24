extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
           'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
           'dezesete', 'dezoito', 'dezenove', 'vinte')
resp = ''
while True:
    num = int(input('Digite um número entre 0 e 20:'))
    while num < 0 or num > 20:
        num = int(input('Número inválido. Tente novamente:'))
    print(f'O número digitado por extenso fica: \033[31m{extenso[num].upper()}\033[m')
    resp = str(input('Você quer continuar?')).upper()[0].strip()
    if resp == 'N':
        break
print('Obrigado por utilizar nosso sistema. Volte sempre!')




