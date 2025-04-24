import random
jogada_computador = random.randint( 1, 3)
print('Bora jogar um JOKEMPO!')
print('''[1] PEDRA
[2] PAPEL
[3] TESOURA. ''')
jogada = int(input('Me diga qual sua jogada?'))
if jogada == 1 and jogada_computador == 1:
    print('Você jogou PEDRA e eu também. Vish, empatamos.')
elif jogada == 2 and jogada_computador == 2:
    print('Você jogou PAPEL e eu também. Vish, empatamos.')
elif jogada == 3 and jogada_computador == 3:
    print('Você jogou TESOURA e eu também. Empatamos.')
elif jogada == 3 and jogada_computador == 2:
    print('Você jogou TESOURA e eu joguei PAPEL. Você venceu!')
elif jogada == 2 and jogada_computador == 1:
    print('Você jogou PAPEL e eu joguei PEDRA. Você venceu!')
elif jogada == 1 and jogada_computador == 3:
    print('Você jogou PEDRA e eu joguei TESOURA. Você venceu!')
elif jogada == 1 and jogada_computador == 2:
    print('Você jogou PEDRA e eu joguei PAPEL. Eu venci haha')
elif jogada == 2 and jogada_computador == 3:
    print('Você jogou PAPEL e eu joguei TESOURA. Eu venci haha')
elif jogada == 3 and jogada_computador == 1:
    print('Você jogou TESOURA e eu joguei PEDRA. Eu venci haha')




