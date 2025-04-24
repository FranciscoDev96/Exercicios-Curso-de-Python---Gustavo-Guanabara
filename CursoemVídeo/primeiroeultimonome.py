nome = str(input('Digite seu nome:')).strip()
print(nome)
a = nome.split()[0]
print(f'Primeiro= {a}')
b = nome.split()[-1]
print(f'Último nome = {b}')

