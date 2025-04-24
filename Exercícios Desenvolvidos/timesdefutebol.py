times = ('Fortaleza', 'Juventude', 'Vasco da Gama',
         'Cruzeiro', 'Grêmio', 'Corinthians', 'Flamengo',
         'Internacional', 'Bahia', 'São Paulo', 'Sport Recife',
         'Botafogo', 'Palmeiras', 'Ceará SC', 'Bragantino',
         'Atlético MG','Santos', 'Mirassol', 'Fluminense', 'EC Vitória')
print(f'Lista de times do Brasileirão Série A: {times}')
print('-=' * 20)
print(f'Os 5 primeiros colocados são: {times[:5]}')
print('-=' * 20)
print(f'Os 4 últimos colocados são: {times[-4:]}')
print('-=' * 20)
print(f'A lista de time em ordem alfabética fica: {sorted(times)}')
print('-=' * 20)
print(f'O Internacional, está na {times.index('Internacional')+1}ª posição.')

