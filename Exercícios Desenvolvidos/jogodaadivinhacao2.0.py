from random import randint
from time import sleep
jogada_computador = randint(1,10)
resposta = str(input('Bora jogar um jogo da adivinhação?')).upper().strip()
while resposta == 'NAO':
    resposta = str(input('Tem certeza? Diz que sim para começarmos?')).upper().strip()
print('Bora jogar!!')
print('\033[30;45mPENSANDO\033[m')
sleep(3)
jogada = int(input('Qual número eu pensei de 1 a 10? Tente acertar em menos de 7 tentativas.'))
total_jogadas = 1
while jogada != jogada_computador or total_jogadas == 7:
    if jogada > jogada_computador:
        jogada = int(input('Menos. Tente novamente:'))
    if jogada < jogada_computador:
        jogada = int(input('Mais. Tente novamente:'))
        total_jogadas += 1
    if total_jogadas == 7:
        print('Já foram 7 tentativas. Você perdeu. Mas continue tentando até acertar:')
print(f'Aeee, você acertou!!\nVocê tentou acertar {total_jogadas} vezes. ')