from time import sleep
num1 = int(input('Digite o 1º número:'))
num2 = int(input('Digite o 2º número:'))
print('''Escolha uma das opções:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair''')
opcao = int(input('Digite sua opção:'))
while opcao != 5:
    if opcao == 1:
        print(f'A soma do números digitados é de {num1 + num2}.')
        print('=' * 20)
        print('''Escolha uma das opções:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair''')
        opcao = int(input('O que você deseja fazer agora?'))
    if opcao == 2:
        print(f'A multiplicação dos números digitados é de {num1 * num2}.')
        print('=' * 20)
        print('''Escolha uma das opções:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair''')
        opcao = int(input('O que deseja fazer agora?'))
    if opcao == 3:
        if num1>num2:
            print(f'O maior número entre os números digitados é o {num1}. ')
        else:
            print(f'O maior número entre os números digitados é o {num2}.')
        print('=' * 20)
        print('''Escolha uma das opções:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair''')
        opcao = int(input('O que deseja fazer agora?'))
    if opcao == 4:
        num1 = int(input('Digite o novo 1º número:'))
        num2 = int(input('Digite o novo 2º número:'))
        opcao = int(input('Entendi. Ja substituí seus números. O que deseja fazer agora?'))
    if opcao > 5:
        print('Opção inválida. Tente novamente.')
        opcao = int(input('O que deseja fazer agora?'))
print('FINALIZANDO')
sleep(3)
print('Programa finalizado. Obrigado!')








