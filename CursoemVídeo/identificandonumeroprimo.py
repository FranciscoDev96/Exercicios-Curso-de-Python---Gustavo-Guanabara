num = int(input('Digite um número:'))
cont = 0
for p in range(1, num+1):
    if num % p == 0:
        print('\033[32m',end=' ')
        cont+= 1
    else:
        print('\033[31m',end= ' ')
    print(f'{p}',end='')
print(f'\n\033[mO número {num} foi divisível {cont} vezes.')
if cont == 2:
    print('E por isso ele é PRIMO.')
else:
    print('E por isso, ele NÃO É PRIMO.')


