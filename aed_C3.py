def num_primo(* lista_numeros):
    lista = []  # lista declarada com list;

    for n in lista_numeros:  # percorre cada número na lista;
        n_divisivel = 0  # contador do número de divisores;
        for c in range(1, n + 1):  # verifica se o número possui mais de um divisor;
            if n % c == 0:
                n_divisivel += 1  # acrescenta 1 ao número de divisores;

        if n_divisivel == 2:  # se o valor estiver com 2 divisores ele é primo;
            lista.append(True)
        else:
            lista.append(False)  # se não, ele não é primo;
    print(lista)  # mostra a lista com os valores Booleanos;


num_primo(2, 3, 5, 7, 11)  # chamar a função e passar parametros.
