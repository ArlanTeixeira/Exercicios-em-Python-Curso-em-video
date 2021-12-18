aluno = {}
aluno['nome'] = str(input('Qual o nome do Aluno: '))
aluno['media']= float(input(f'Qual a média do {aluno["nome"]}: '))
if aluno['media'] < 5:
    aluno['situacao'] = 'Reprovado'
else:
    aluno['situacao'] = 'Aprovado'
print(f'Nome do aluno: {aluno["nome"]}')
print(f'A média do aluno é: {aluno["media"]}')
print(f'Situação: {aluno["situacao"]}')
