def voto(ano):
    from datetime import datetime
    n = datetime.today().year - ano
    if 65 > n >= 18 :
        return f'Com {n} anos:VOTO OBRIGATÓRIO'

    elif n < 16:
        return f'Com {n} anos: NÃO PODE VOTAR'

    if  16 <= n < 18 or n > 65:
        return f'Com {n} anos: VOTO OPCIONAL'

nasc = int(input('Em que ano você nasceu?'))
print(voto(nasc))


