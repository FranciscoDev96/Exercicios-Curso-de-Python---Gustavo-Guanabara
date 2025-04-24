import random
from time import sleep
num = random.randint(0,5)
print('-+-' * 20)
print('Hey, acabei de pensar em número entre 0 e 5.')
print('-+-' * 20)
resposta = int(input('Digite o número que você acha que pensei:'))
print('ANALISANDO SUA RESPOSTA')
sleep(3)
if num == resposta:
    print('Parabéns. Você venceu.')
else:
    print(f'Eu ganhei. Eu pensei no número {num}. E não no número {resposta}')









