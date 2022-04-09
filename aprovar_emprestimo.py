import time

nome = input('Digite seu nome: ')

casa = float((input('Digite o valor da casa: ')))

salario = float(input('Digite o valor do seu salário: '))

anos = float(input('Digite em quantos anos deseja pagar o empréstimo Sr(a) {}: '.format(nome)))
prestacao = casa / (anos * 12)

print('Para pagar uma casa de {:.2f} em {:.0f} anos você pagará {:.2f} por mês.'.format(casa,anos, prestacao))

print('Lembrando que o valor do empréstimo não pode exceder 30% \n'
      'do seu salário, caso o faça, seu empréstimo será negado.')

minimo = salario * (30/100)

time.sleep(2)
print('PROCESSANDO...')

if prestacao <= minimo:
      print('Seu empréstimo foi aprovado.')
else:
      print('O seu empréstimo foi negado!')

print('É sempre um prazer atende-lo, volte sempre {}!'.format(nome))
