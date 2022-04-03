nome = input("Digite seu nome:")

nota1 = float(input("digite a primeira nota:"))

nota2 = float(input("digite a segunda nota:"))

nota3 = float(input("digite a terceira nota:"))

media = (nota1 + nota2 + nota3) / 3

if media>= 7:
    print(nome, "Aprovado")
else:
    if media <=5:
        print(nome, "Reprovado")
    else:
        print(nome, "Recuperação")



