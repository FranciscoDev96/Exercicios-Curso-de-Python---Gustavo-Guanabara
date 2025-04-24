lista = []
cont = 0
while True:
    n = int(input('Digite um número:'))
    lista.append(n)
    cont+= 1
    resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
print(f'Foram digitados {cont} números.')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente fica: {lista}.')
if 5 in lista:
   print(f'O número 5 foi digitado e aparece na {lista.index(5)+1}ª posição da lista.')
else:
    print('O número 5 não foi digitado.')

