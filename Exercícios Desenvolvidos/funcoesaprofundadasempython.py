def leiaInt(msg):
    try:
        valor = 0
        okay = False
        while True:
            n = str(input(msg))
            if n.isnumeric():
                valor = int(n)
                okay = True
            else:
                print('\033[0;31mERRO! Digite um número inteiro válido: \033[m')
            if okay is True:
                break
    except KeyboardInterrupt:
        valor = 0
        print('\nO usuário optou por não digitar os dados.')
    return valor

def is_numeric(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False

def leiaFloat(msg):
    try:
        valor = 0
        ok = False
        while True:
            n = str(input(msg))
            if is_numeric(n):
                valor = float(n)
                ok = True
            else:
                print('\033[31mErro! Digite um número real válido:\033[m')
            if ok is True:
                break
    except KeyboardInterrupt:
        valor = 0
        print('\n\033[35mO usuário optou por não digitar os dados.\033[m')
    return valor

i = leiaInt('Digite um número inteiro:')
r = leiaFloat('Digite um número real:')
print(f'O número inteiro digitado foi {i} e o real foi {r} .')