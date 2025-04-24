lista = []
e = str(input('Digite a expressão:'))
lista.append(e)
pa = e.count('(')
pf = e.count(')')
if pa == pf:
    print('Expressão válida.')
else:
    print('Expressão inválida.')

