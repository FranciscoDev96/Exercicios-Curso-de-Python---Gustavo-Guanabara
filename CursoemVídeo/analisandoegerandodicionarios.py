def notas(*num, sit = False):
    """
    Função que calcula a média, mostra a maior e menor nota e também, mostra a situação da turma (Opcional).
    :param num: Número de notas a serem analisadas. Aceita várias.
    :param sit: (Opcional). Mostra qual a situação da turma (Ruim (Abaixo de 5), Razoável (Entre 5 e 7), Boa (Acima de 7)), baseado na média.
    :return: Retorna um dicionário com todas as informações citadas acima.
    """
    turma = dict()
    turma["Maior"] = max(num)
    turma["Menor"] = min(num)
    turma["Total"] = len(num)
    turma["Média"] = sum(num) / len(num)
    if sit:
        if turma["Média"] >= 7:
            turma["Sit"] = 'Boa'
        elif 5 <= turma["Média"] < 7:
            turma["Sit"] = 'Razoável'
        else:
            turma["Sit"] = 'Ruim'
    return turma


resp = notas(5.5, 2.5, 1.5 ,sit=True)
print(resp)
help(notas)