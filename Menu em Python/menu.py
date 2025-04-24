import uteis
import arquivo

arq = 'menuempython.txt'

if not arquivo.arquivoexiste(arq):
    arquivo.criararquivo(arq)

while True:
    opc = uteis.menu(['Ver pessoas cadastradas', 'Cadastrar Nova Pessoa', 'Sair do Sistema'])
    if opc == 1:
        arquivo.lerArquivo(arq)
    elif opc == 2:
        uteis.cabeçalho('NOVA PESSOA')
        nome = str(input('Nome:'))
        idade = uteis.leiaInt('Idade:')
        arquivo.cadastrar(arq, nome, idade)
    elif opc == 3:
        uteis.cabeçalho('\033[35mFinalizando o Sistema... Volte sempre\033[m')
        break
    else:
        print('\033[31mInforme uma opção válida.\033[m')

