seg1 = float(input('Qual o primeiro segmento?'))
seg2 = float(input('Qual o segundo segmento?'))
seg3 = float(input('Qual o terceiro segmento?'))
if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Com esses valores você pode formar um triângulo', end=' ')
    if seg1 == seg2 == seg3:
        print('EQUILATERO.')
    elif seg1 == seg2 or seg2 == seg3 or seg1 == seg3:
        print('ISÓSCELES. ')
    else:
        print('ESCALENO.')
else:
    print('Com esses valores, você não pode formar um triângulo.')



