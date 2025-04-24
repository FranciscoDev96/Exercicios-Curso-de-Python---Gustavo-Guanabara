from random import randint
from time import sleep

numeros = []
def sorteio():
    print('Sorteando 5 valores da lista:', end='')
    for c in range(0, 5):
        num = randint(0,10)
        print(num, end=' ')
        sleep(0.5)
        numeros.append(num)
    print('Pronto!')
def somapar():
    soma = 0
    for num in numeros:
        if num % 2 == 0:
            soma += num
    print(f'Somando os valores pares de {numeros} , temos {soma}.')


sorteio()
somapar()