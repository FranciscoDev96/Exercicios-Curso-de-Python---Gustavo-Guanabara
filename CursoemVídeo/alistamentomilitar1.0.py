ano = int(input('Digite o seu ano de nascimento:'))
genero = str(input('Qual seu genêro. Digite (M) para masculino e (F) para feminino:')).strip().upper()
alistamento = 2025 - ano
tempo_passou = alistamento - 18
tempo_faltante = 18 - alistamento
deveria_alistado = 2025 - tempo_passou #ano
deveria_alistar = 2025 + tempo_faltante
if alistamento > 18 and genero == 'M':
    print(f'Quem nasceu em {ano} tem {alistamento} anos em 2025. \nSe passaram {tempo_passou} anos. \nSeu alistamento foi em {deveria_alistado}.')
elif alistamento < 18 and genero == 'M':
    print(f'Quem nasceu em {ano} tem {alistamento} anos em 2025. \nAinda faltam {tempo_faltante} anos. \nSeu alistamento será em {deveria_alistar}')
elif alistamento == 18 and genero == 'M':
    print(f'Quem nasceu em {ano} tem {alistamento} anos em 2025. Você tem que se alistar IMEDIATAMENTE.')
elif genero == 'F':
    print(f'Você não precisa se alistar!')

