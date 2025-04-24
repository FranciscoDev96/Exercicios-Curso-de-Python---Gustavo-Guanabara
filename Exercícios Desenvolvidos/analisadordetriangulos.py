linha1 = float(input('Qual o primeiro segmento?'))
linha2 = float(input('Qual o segundo segmento?'))
linha3 = float(input('Qual o terceiro segmento?'))
if linha1 < linha2 + linha3 and linha2 < linha1 + linha3 and linha3 < linha1 + linha2:
    print('Esses segmentos FORMAM um triângulo')
else:
    print('Esses segmentos NÃO FORMAM um triângulo')
