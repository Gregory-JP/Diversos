# Exercicio B1 - AED
def teste(* lista):
    i = diferenca = 0
    p = 1

    maior_dif = maior_dif2 = diferenca
    v1 = v2 = v3 = v4 = 0

    while True:
        try:
            diferenca = lista[i] - lista[p]

            if diferenca >= maior_dif:
                v1 = lista[i]
                v2 = lista[p]
                maior_dif = diferenca

            if diferenca < maior_dif2:
                v3 = lista[i]
                v4 = lista[p]
                maior_dif2 = diferenca

            i += 1
            p += 1
        except IndexError:
            break
    if abs(maior_dif) > abs(maior_dif2):
        print(f'A maior diferença é entre {v1} e {v2}, que resulta em |{maior_dif}|.')
        print(f'A segunda maior diferença é entre {v3} e {v4}, que resulta em |{abs(maior_dif2)}|.')

    else:
        print(f'A maior diferença é entre {v3} e {v4}, que resulta em |{abs(maior_dif2)}|.')
        print(f'A segunda maior diferença é entre {v1} e {v2}, que resulta em |{maior_dif}|.')


teste(10,20,40,60)
