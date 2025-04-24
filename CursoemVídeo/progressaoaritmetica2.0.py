primeiro = int(input('Digite o primeiro termo:'))
razao = int(input('Digite a razao:'))
termo = primeiro
cont = 1
while cont <=11:
    print(f'{termo} - ', end=' ')
    termo += razao
    cont += 1
    if cont == 11:
        adc = int(input('PAUSA.\nQuantos termos a mais você quer mostrar? Digite 0 para sair:'))
        cont = 1
        while cont <= adc:
            print(f'{termo} - ', end=' ')
            termo += razao
            cont += 1
            if cont == adc+1:
                adc = int(input('PAUSA.\nQuantos termos a mais você quer mostrar? Digite 0 para sair:'))
                cont = 1
            if adc == 0:
                cont = cont + 20
                print('FINALIZANDO...')
print('Programa finalizado. Obrigado!')


