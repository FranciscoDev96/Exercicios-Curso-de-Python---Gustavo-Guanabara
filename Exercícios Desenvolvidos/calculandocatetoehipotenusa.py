from math import hypot
a = float(input('Digite o cateto adjacente:'))
b = float(input('Digite o cateto oposto:'))
c = hypot(a ,b)
print(f'Quando o cateto oposto é {b}, e o cateto adjacente é {a} \nA hipotenusa será {c:.2f}')



