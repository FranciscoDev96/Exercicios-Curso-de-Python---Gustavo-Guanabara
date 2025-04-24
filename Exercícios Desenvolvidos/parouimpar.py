from random import randint
cont = -1
while True:
    jogada_computador = randint(0, 10)
    jogada = int(input('Qual número você quer jogar?'))
    opcao = str(input('Você quer par ou ímpar? [I/P]')).upper()[0].strip()
    soma = jogada_computador + jogada
    if opcao == 'P':
        if soma % 2 == 0:
            print(f'Você VENCEU. Eu joguei {jogada_computador}. A soma dos dois números foi de {soma}. Um número PAR.')
    if opcao == 'I':
        if soma % 2 == 1:
            print(f'Você VENCEU. Eu joguei {jogada_computador}. A soma dos valores foi de {soma}. Portanto um número IMPAR.')
    if opcao == 'P':
        if soma % 2 == 1:
            print(f'Você PERDEU. Eu joguei {jogada_computador}. A soma dos dois números foi de {soma}. Um número IMPAR.')
            jogada_computador ='Vit'
    if opcao == 'I':
         if soma % 2 == 0:
            print(f'Você PERDEU. Eu joguei {jogada_computador}. A soma dos dois números foi de {soma}. Um número PAR.')
            jogada_computador ='Vit'
    cont += 1
    if opcao != 'I' and opcao != 'P':
        print('Opção INVALIDA. Jogue novamente.')
        cont -= 1
    if jogada_computador == 'Vit':
        break
print(f'GAME OVER! Você venceu {cont} vezes.')

