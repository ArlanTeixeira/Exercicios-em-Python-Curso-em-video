pessoas = list()
dado = list()
contp = 0
maiorPeso = 0
menorPeso = 0
while True:
    dado.append(str(input('Digite o nome da Pessoa: ')))
    dado.append(int(input('Agora digite o peso da Pessoa: ')))
    pessoas.append(dado[:])
    dado.clear()
    contp += 1
    r = str(input('Deseja continuar? [S/N]'))
    if r in 'Nn':
        break
pessoaGorda = list()
pessoaMagra = list()
for p in pessoas:
    if p[1] > 100:
        pessoaGorda.append(p[0])
    elif p[1] < 80:
        pessoaMagra.append(p[0])

print('=' * 20, 'Cadastro de pessoas', '=' * 20)
print(pessoas)
print(f'Você cadastrou {contp} pessoas')
print(f'Essas são as pessoas acima de 100kg:  {pessoaGorda}')
print(f'Essas são as pessoas com menos de 70kg: {pessoaMagra}')
