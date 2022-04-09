from itertools import product

quant_num = int(input('Qual o alcance da combinação? Ex.: de 0 a 10...(0,10) '))
caracteres = range(0,quant_num + 1)
list_perms = []
quant = int(input('Quantos números deve ter a sequência? Ex.: 01,001,0001... '))
num_comb = product(caracteres, repeat=quant)  # quantidade de números da sequência

for subset in num_comb:
    print(subset)  # tupla retornada com uma combinação por loop
    list_perms.append(subset)
