A = float(input('Primeiro segmento: '))
B = float(input('Segundo segmento: '))
C = float(input('Terceiro segmento: '))

if A < B + C and B < A + C and C < A + B:
    print('Os valores informados formam um triângulo.')
    if A == B == C:
        print('Você formou um triângulo equilátero.')
    elif A != B != C != A:
        print('Você formou um triângulo escaleno.')
    else:
        print('Você formou um triângulo isósceles.')
else:
    print('Os segmentos não formam triângulo!')
