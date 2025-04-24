from datetime import datetime
dados = dict()
dados['Nome'] = str(input('Nome:'))
dados['Idade'] = int(input('Ano de nascimento:'))
anos = datetime.today().year - dados['Idade']
dados['Idade'] = anos
dados['CTPS'] = str(input('Carteira de trabalho (0 não tem):'))
if dados['CTPS'] == '0':
    for k, v in dados.items():
        print(f'{k} tem valor {v}.')
else:
    dados['Ano de contratação'] = int(input('Ano de contratação:'))
    anos_trabalhado = datetime.today().year - dados["Ano de contratação"]
    anos_ate_aposentadoria = 35 - anos_trabalhado
    dados['Aposentadoria'] = anos + anos_ate_aposentadoria
    dados['Salário'] = float(input('Salário:'))
    for k, v in dados.items():
        print(f'  -{k} tem valor {v}')


