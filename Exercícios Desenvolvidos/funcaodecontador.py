def contador ():
    print(f'Contagem de 1 até 10 de 1 em 1:')

    for c in range(1, 11):
        print(f'{c}', end=' ')

    print('FIM')
    print('-'*30)
    print('Contagem de 10 até 0 de 2 em 2:')
    for c in range(10, -1, -2):
        print(f'{c}', end=' ')

    print('FIM')
    print('-' * 30)
    print('Agora é a sua vez de personalizar a contagem:')

def contador2(a,b,d):
    for c in range(a,b,d):
        print(f'{c}', end=' ')
    if d == 0:
        d = 1
        for c in range(a, b, d):
            print(f'{c}', end=' ')
    if a > b:
        d -= d*2
        for c in range(a, b, d):
            print(f'{c}', end=' ')


contador()
i = int(input('Início:'))
f = int(input('Fim:'))
p = int(input('Passo:'))
print(f'Contagem de {i} até {f} de {p} em {p}:')
contador2(i,f,p)





