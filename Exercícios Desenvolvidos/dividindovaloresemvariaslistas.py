lista = []
par = []
impar = []
while True:
    n = int(input('Digite um número:'))
    lista.append(n)
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
for n in lista:
    if n % 2 == 0:
       par.append(n)
    else:
        impar.append(n)
print(f'Os números digitados foram {lista}.')
print(f'Os números pares digitados foram {par}.')
print(f'Os números ímpares digitados foram {impar}.')



