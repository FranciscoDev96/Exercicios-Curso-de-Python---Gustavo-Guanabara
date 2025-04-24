def ajuda(msg):
        return help(msg)




while True:
    print('\033[97;42m~' * 30)
    print('\033[97;42m  Sistema de ajuda do PyThon:')
    print('\033[97;42m~' * 30)
    opc = str(input('\033[mFunção ou Biblioteca:')).lower()
    if opc == 'fim':
        break
    print('\033[0;97;44m~' * 30)
    print(f'\033[0;97;44m  Acessando dados de: {opc}')
    print('\033[0;97;44m~' * 30)
    print('\033[0;30;107m')
    ajuda(opc)
print('\033[0;97;41m~' * 36)
print('\033[0;97;41m  Obrigado por usar nosso sistema')
print('\033[0;97;41m~' * 36)