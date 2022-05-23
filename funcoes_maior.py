def maior(* numeros):
    cont = m = 0
    print(f'{"Analisando os valores recebidos...":>50}'.upper())
    print('-=' * 18)
    for n in numeros:
        print(f'{n} ',end=' ')
        if cont == 0:
            m = n
        else:
            if n > m:
                m = n
        cont += 1
    print(f'\nForam informados {cont} valores ao todo.')
    print('*' * 34)
    print(f'O maior valor informado é {m}.')
    print('*' * 34)


maior(4, 5, 10, 64, 9, 6, 18, 21, 30)
maior(100, 2, 6, 10, 8, 0, 12, 18, 120, 208)
maior(-2, -10, -26, 0, 4, 9, 11, 14, -2, 91, 1)
maior(8)
maior()
