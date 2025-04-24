matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
num_coluna2 = []
soma = soma3coluna = cont = cont_linha = 0
for l in range(0,3):
    cont_linha += 1
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para {l}, {c}:'))
        if matriz[l][c] % 2 == 0:
            soma+=matriz[l][c]
        cont+=1
        if cont == 3:
            soma3coluna+=matriz[l][c]
        if cont_linha == 2:
            num_coluna2.append(matriz[l][c])
    cont = 0
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
print(f'A soma dos números pares da matriz é: {soma}.')
print(f'A soma dos números digitados na terceira coluna é de: {soma3coluna}.')
print(f'O maior número da segunda linha é: {max(num_coluna2)}.')

