import math
angulo_graus = float(input('Digite um ângulo para calcular o seno, cosseno e tangente:'))
angulo_radianos = math.radians(angulo_graus)
seno = math.sin(angulo_radianos)
cosseno = math.cos(angulo_radianos)
tangente = math.tan(angulo_radianos)
print(f'O seno do {angulo_graus} é de {seno:.2f}. \nO cosseno de {angulo_graus} é de {cosseno:.2f}. \nA tangente de {angulo_graus} é de {tangente:.2f}')


