def area(larg, comp):
    print(f'A largura é {larg}m e o comprimento é {comp}m;')
    a = larg * comp
    print(f'A área do seu terreno é {a} m².')


la = float(input('Qual a largura com terreno? '))
com = float(input('Qual o comprimento do terreno? '))
area(la, com)
