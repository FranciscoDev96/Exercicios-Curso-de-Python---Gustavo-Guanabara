def fatorial(num, show= False):
    """
    Calcula o Fatorial de um número.
    :param num: Número a ser calculado.
    :param show: (Opcional) Se deseja mostrar o cálculo ou não.
    :return: Retorna o fatorial de um número num.
    """
    f = 1
    for c in range(num, 0, -1):
       if show:
            print(c, end='')
            if c > 1:
                print(' X ', end='')
            else:
                print(' = ', end='')
            f *= c
    return f
print(fatorial(10, show=False))
