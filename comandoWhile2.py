numero = 0

de0a25 = 0
de26a50 = 0
de51a75 = 0
de76a100 = 0

while numero >=0:
    numero = int(input("Digite um valor:"))

    if numero >=0:
        if numero <= 25:
            de0a25 += 1
        else:
            if numero <= 50:
                de26a50 += 1
            else:
                if numero <= 75:
                    de51a75 += 1
                else:
                    if numero <= 100:
                        de76a100 += 1

print(de0a25)
print(de26a50)
print(de51a75)
print(de76a100)
