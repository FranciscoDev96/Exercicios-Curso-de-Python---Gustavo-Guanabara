num = int(input('Qual valor você quer saber a tabuada?'))
while True:
    print('-' * 30)
    if num < 0:
        break
    else:
        cont = 0
        while cont < 10:
            cont += 1
            print(f'{num} X {cont} = {num * cont}')
        print('-' * 30)
        num = int(input('Digite outro valor:'))
print('Programa encerrado. Volte sempre!')
