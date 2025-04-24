def area(a, b):
    terreno = b*a
    print(f'A área de um terreno {a:.1f} X {b:.1f} é de {terreno:.1f}m².')


print('CONTROLE DE TERRENOS')
print('-'*30)
l = float(input('Largura(m):'))
c = float(input('Comprimento(m):'))
area(l,c)