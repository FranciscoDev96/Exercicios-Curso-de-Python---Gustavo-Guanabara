def cabeçalho(msg):
    print('-'*42)
    print(msg.center(42))
    print('-'*42)

def linha():
    print('-' * 42)

def menu(msg):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in msg:
        print(f'\033[33m{c} - \033[34m{item}\033[m')
        c +=1
    linha()
    resposta = leiaInt('\033[33mSua opção:\033[m')
    return resposta

def leiaInt(num):
        while True:
            try:
                n = int(input(num))
            except (ValueError, TypeError):
                print('\033[31mDados inválidos. Tente novamente\033[m')
                continue
            except KeyboardInterrupt:
                print('\n\033[31mO usuário preferiu não informar os dados.\033[m')
            else:
                return n








