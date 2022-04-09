def notas(*n, sit=False):
    """
    -> Função que gera um dicionário para analisar situações de alunos;
    :parâmetro n: uma ou mais notas do aluno;
    :parâmetro sit: valor opcional, indica a situação escolar do aluno;
    :return: retorna um dicionário com todos os dados;
    """
    boletim = {'Total': len(n), 'Maior': max(n), 'Menor': min(n), 'Media': sum(n)/len(n)}
    if sit:
        if boletim['Media'] >= 7:
            boletim['Situação']= 'BOA'
        elif boletim['Media'] >= 5:
            boletim['Situação'] = 'RAZOÁVEL'
        else:
            boletim['Situação'] = 'RUIM'
    return boletim


b = notas(6, 10, 6, 9.5,sit=True)
print(b)
help(notas)
