from random import randint
from time import sleep
lista = []
jogos = []
cont = 0
tot = 1
print('     JOGO DA MEGA SENA     ')
quant = int(input('Quantos jogos você quer que eu faça:'))
print('-='* 30)
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot+=1
print(f'GERANDO {quant} JOGOS')
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('-='*10,'Boa Sorte','-='*10)






