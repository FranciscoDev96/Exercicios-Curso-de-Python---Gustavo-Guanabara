frase = str(input('Digite uma frase:')).upper().strip()
frase.count('a' )
print(f'A frase digitada possui: {frase.count('A')} letras a.')
p1 = frase.find('A')+1
print(f'A letra a aparece na posição {p1}, pela primeira vez.')
p2 = frase.rfind('A')+1
print(f'A letra a aparece pela última vez, na posição {p2}')
