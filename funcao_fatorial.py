def fatorial(numero, show=False):
    """
    -> Calcula o fatorial de um número;
    :parâmetro n: valor a ser calculado;
    :parâmetro show:(Opcional), mostra o calculo;
    :return: retorna o resultado do Fatorial de n;
    """
    f = 1
    for cont in range(numero,0,-1):
        if show:
            print(cont, end=' ')
            if cont > 1:
                print('x', end=' ')
            else:
                print(f' = ',end=' ')
        f*= cont
    return f


print(fatorial(5, True))
