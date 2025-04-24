from random import randint
from time import sleep
from operator import itemgetter
jogadas = {'Jogador 1': randint(1, 6),
           'Jogador 2': randint(1, 6),
           'Jogador 3': randint(1, 6),
           'Jogador 4': randint(1, 6)}
ranking = list()
print('Valores sorteados')
for k, v in jogadas.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(jogadas.items(), key=itemgetter(1), reverse = True)
print('-='*30)
print(' == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'   {i+1}º lugar: {v[0]} com {v[1]}.')
print('-='*30)
if jogadas['Jogador 1'] > jogadas['Jogador 2'] and jogadas['Jogador 1'] > jogadas['Jogador 3'] and jogadas['Jogador 1'] > jogadas['Jogador 4']:
    print('Jogador 1 é o vencedor!')
if jogadas['Jogador 2'] > jogadas['Jogador 1'] and jogadas['Jogador 2'] > jogadas['Jogador 3'] and jogadas['Jogador 2'] > jogadas['Jogador 4']:
    print('Jogador 2 é o vencedor!')
if jogadas['Jogador 3'] > jogadas['Jogador 1'] and jogadas['Jogador 3'] > jogadas['Jogador 2'] and jogadas['Jogador 3'] > jogadas['Jogador 4']:
    print('Jogador 3 é o vencedor!')
if jogadas['Jogador 4'] > jogadas['Jogador 1'] and jogadas['Jogador 4'] > jogadas['Jogador 2'] and jogadas['Jogador 4'] > jogadas['Jogador 3']:
    print('Jogador 4 é o vencedor!')