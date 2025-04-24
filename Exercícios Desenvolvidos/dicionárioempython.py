alunos = dict()
alunos['Nome'] = str(input('Nome do aluno:'))
alunos['Media'] = float(input(f'Media do {alunos["Nome"]}:'))
for k, v in alunos.items():
    print(f' -{k} é igual a {v}')
if alunos['Media'] >= 7:
    print(' -Situação é igual a aprovado')
elif 5 < alunos['Media'] < 7:
    print(' -Situação é igual a recuperação.')
else:
    print(' -Situação é igual a reprovado')
