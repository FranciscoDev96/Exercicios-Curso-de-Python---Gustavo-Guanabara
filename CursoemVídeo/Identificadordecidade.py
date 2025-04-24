cidade = str(input('Digite o nome da sua cidade:')).strip()
a = cidade.split()
b = a[0]
d = b.upper()
c = 'SANTO' in d
print(f'A cidade {cidade} tem Santo no início do nome?: {c}')



