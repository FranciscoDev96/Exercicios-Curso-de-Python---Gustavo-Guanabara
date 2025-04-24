from datetime import datetime
data = str(input('Digite sua data de nascimento:'))
data2 = datetime.strptime(data, '%d/%m/%Y')
hoje = datetime.today()
alistamento = hoje.year - data2.year #Sabe que é 18 anos
tempo_passou =  alistamento - 18
tempo_faltante = 18 - alistamento
if alistamento > 18:
    print(f'Você esta atrasado {tempo_passou} anos.')
elif alistamento < 18:
    print(f'Ainda faltam {tempo_faltante} anos para você se alistar. ')
elif alistamento == 18:
    print(f'Você está dentro do período de alistamento.')











