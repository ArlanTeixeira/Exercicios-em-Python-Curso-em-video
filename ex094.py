dados = dict()
pessoas = list()
mulheres = list()
pmedia = list()
totalidade = 0
media = 0
while True:
    dados['nome'] = str(input('Digite o nome da pessoa: '))
    while True:
        dados['sexo'] = str(input('Digite o Sexo da pessoa: [M/F]')).upper()[0]
        if dados['sexo'] in 'MF':
            break
        print('Erro! Digite apenas M ou F')
    dados['idade'] = int(input('Digite a idade da pessoa: '))
    pessoas.append(dados.copy())
    totalidade += dados['idade']
    media = totalidade / len(pessoas)
    if dados['sexo'] in 'Ff':
        mulheres.append(dados['nome'])
    while True:
        r = str(input('Deseja continuar? [S/N]')).upper()[0]
        if r in 'SN':
            break
        print('Erro! Digite apenas S ou N')
    if r == 'N':
        break
if dados['idade'] > media:
    pmedia.append(dados.copy())
print(f'Total de pessoas cadastradas: {len(pessoas)}')
print(f'Média de idade: {media}')
print(f'Essas são as mulheres do grupo: {mulheres}')
print('Pessoas acima da média: ')
for pm in pmedia:
    print(f'Nome:{pm["nome"]}, Sexo: {pm["sexo"]}, Idade {pm["idade"]}')
