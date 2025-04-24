from time import sleep
alunos = []
notas = []
grupo = []
grupao = []
media = 0
print('    Cadastro de Alunos    ')
while True:
    nome = str(input('Nome:'))
    alunos.append(nome)
    nota1 = float(input('Nota 1:'))
    notas.append(nota1)
    nota2 = float(input('Nota 2:'))
    notas.append(nota2)
    grupo.append(alunos[:])
    grupo.append(notas[:])
    grupao.append(grupo[:])
    notas.clear()
    alunos.clear()
    grupo.clear()
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('No.', end='    ')
print(f'{"Nome":<10}', end='')
print(f'{"MÉDIA":>20}')
print('-'*40)
for n, a in grupao:
    media = (a[0] + a[1]) / 2
for n, a in enumerate(grupao):
    print(f'{n}',end='     ')
    print(f'{a[0]}',end='   ')
    print(f'{media:>20.1f}')
r = int(input('Qual aluno você gostaria de ver a nota? (999) interrompe:'))
while r != 999:
    for n, a in enumerate(grupao):
        if r == n or r == 1:
            print(f'Notas de {a[0]} são {a[1]}.')
            print('-' * 30)
            r = int(input('Qual aluno você gostaria de ver a nota? (999) interrompe:'))
        elif n < r < 999:
            print('Opção Inválida. Tente novamente.')
            print('-' * 30)
            r = int(input('Qual aluno você gostaria de ver a nota? (999) interrompe:'))
print('-'*30)
print('FINALIZANDO...')
sleep(2)
print('Obrigado! Volte Sempre.')







