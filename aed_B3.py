def codigo(palavra, chave):

    alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    nova_palavra = ""  # receberá a nova palavra codificada;
    p = len(palavra)  # ler o tamanho da palavra digitada;

    for i in range(p):
        caractere = palavra[i]  # recebe cada letra da palavra e armazena;
        letra = alfabeto.find(caractere)  # procura a letra armazenada no 'caractere';
        nova_letra = (letra + chave) % 26  # substitui a letra armazenada por a que está a n posições a frente(chave);
        nova_palavra += alfabeto[nova_letra]  # a nova palavra será armazenada aqui, já codificada;
    print(nova_palavra)  # mostra a palavra codificada.


word = (input('Digite a palavra a ser codificada: ')).upper()  # pede a palavra a ser codificada;
key = int(input('Posição das letras: '))  # o número de letras a frente da que deve ser substituida;
codigo(word, key)  # chama a função.
