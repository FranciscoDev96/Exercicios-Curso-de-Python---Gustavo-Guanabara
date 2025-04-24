palavras = ('Basquete', 'Carro', 'Sirene',
            'Corrida', 'Musculaçao','Hipertrofia',
            'Organela', 'Adenosina', 'Miofibrila')
for c in palavras:
    print(f' \nNa palavra {c.upper()} temos as vogais', end= ' ')
    for letra in c:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')

