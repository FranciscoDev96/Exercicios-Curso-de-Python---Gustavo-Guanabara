peso = float(input('Digite seu peso em Kg:'))
altura = float(input('Digite sua altura em m:'))
imc = peso / altura**2
if imc <= 18.5:
    print(f'O seu IMC foi de \033[4;34m{imc:.1f}\033[m. Classificando na tabela geral, você se encontra \033[4;34mabaixo\033[m do peso normal.')
elif imc <=25:
    print(f'O seu IMC foi de \033[4;34m{imc:.1f}\033[m. Classificando na tabela geral, você se encontra no peso \033[4;34mnormal\033[m.')
elif imc <= 30:
    print(f'O seu IMC foi de \033[4;34m{imc:.1f}\033[m. Classificando na tabela, você se encontra com \033[4;34mExcesso de peso\033[m.')
elif imc <= 35:
    print(f'O seu IMC foi de \033[4;34m{imc:.1f}\033[m. Classificando na tabela, você se encontra com \033[4;34mObesidade tipo 1\033[m.')
elif imc <= 40:
    print(f'O seu IMC foi de \033[4;34m{imc:.1f}\033[m. Classificando na tabela, você se encontra com \033[4;34mObesidade tipo 2\033[m.')
elif imc > 40:
    print(f'O seu IMC foi de \033[4;34m{imc:.1f}\033[m. Você esta maluco rapaz? Quer cumer o mundo? Você esta com \033[4;34mObesidade tipo 3\033[m.')



