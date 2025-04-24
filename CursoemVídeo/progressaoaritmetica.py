primeiro_termo = int(input('Digite o 1º termo da PA:'))
razao = int(input('Digite a razão da PA:'))
for pa in range (0, 10):
    prog = primeiro_termo + razao * pa
    print(prog, '-', end= ' ')
print('ACABOU')




