#Calculadora Python ♥♥♥
##########################

#Perguntar para o usuario qual tipo de operação
#Perguntar o primeiro numero
#Perguntar o segundo numero
#Calcular esses 2 numeros
#Imprimir o resultado na tela

import math

print("Olá, bem vindo a calculadora Python:")

while True:

  operacao = input("Qual operação você deseja fazer (+),(-),(*),(/),(**),(numero1 ** 0.5 para raiz), ou \'sair\'/\'exit\' para fechar: ")
  if operacao == 'sair'or operacao == 'exit':
      break
  elif operacao == "+" or operacao == "-" or operacao == "*" or operacao == "/" or operacao == "**":
   numero1 = float(input("Digite um numero: "))
   numero2 = float(input("Digite outro numero: "))
  else:
      print("Operação Invalida")

  if operacao == "+":
      soma = numero1 + numero2
      print(soma)
  elif operacao == "-":
      subtracao = numero1 - numero2
      print(subtracao)
  elif operacao == "*":
      multiplicacao = numero1 * numero2
      print(multiplicacao)
  elif operacao == "/":
      divisao = numero1 / numero2
      print(divisao)
  elif operacao == "**":
      potencia = numero1 ** numero2
      print(potencia)
