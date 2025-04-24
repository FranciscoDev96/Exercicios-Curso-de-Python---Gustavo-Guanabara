time = []
dados = dict()
partidas = list()
while True:
    dados['Jogador'] = str(input('Qual o nome do jogador?'))
    tot = int(input(f'Quantas partidas {dados["Jogador"]} jogou?'))
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols fez na partida {c+1}?:')))
    dados['Gols'] = partidas[:]
    dados['total'] = sum(partidas)
    partidas.clear()
    time.append(dados.copy())
    resp = str(input('Deseja continuar? [S/N]:'))
    print('-='*30)
    if resp in 'Nn':
        break
print(f'cod nome{"gols":>15}{"Total":>20}')
print('-'*50)
for i, v in enumerate(time):
    print(f'{i}', end='   ')
    print(f'{time[i]["Jogador"]}',end='        ')
    print(f'{time[i]["Gols"]}', end='                    ')
    print(f'{time[i]["total"]}')
print('-='*30)
while True:
    opc = int(input('Mostrar Levantamento de qual jogador? (999 interrompe):'))
    print('-='*30)
    if opc <= len(time):
        print(f' --Mostrando dados do jogador {time[opc]["Jogador"]}:')
        for i, v in enumerate(time[opc]["Gols"]):
            print(f'     Na partida {i+1} fez {v} gols.')
    elif 999 > opc > len(time):
        print('ERRO. Digite uma opção válida.')
    if opc == 999:
        break
print('FINALIZANDO...')
print('>>>OBRIGADO!<<<')











