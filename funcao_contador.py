from time import sleep


def contador(i, f, p):
    '''
        param i: valor de inicio do contador
        param f: valor final do contador
        param p: passo do contador
    '''

    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    print('~' * 32)
    print(f'Contagem de {i} até {f} de {p} em {p};')
    sleep(2.5)

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}',end=' ')
            sleep(0.5)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}',end=' ')
            sleep(0.5)
            cont -= p
        print('FIM!')

help(contador)

contador(10, 0, 2)