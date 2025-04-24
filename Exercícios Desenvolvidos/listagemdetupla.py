listagem = ('Lápis', 1.00, 'Lapiseira', 6.90, 'Caderno', 24.90,
            'borracha', 3.90, 'mochila', 129.90, 'Fichàrio', 59.90,
            'Cartolina', 0.99, 'Caderno de desenho', 12.90, 'Lapis de cor', 8.90)
print('-' * 40)
print(f'{"Vendinha do Chico":^40}')
print('-' * 40)
for c in range(0, len(listagem)):
    if c % 2 == 0:
        print(f'{listagem[c]:.<30}', end= ' ' )
    else:
        print(f'R${listagem[c]:>6.2f}')
print('-' * 40)
