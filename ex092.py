import datetime
dados = dict()
dados['nome'] = nome = str(input('Por favor, informe o nome da pessoa: '))
datanas = int(input('Informe agora a data de nascimento: [0000]'))
dados['CTPS'] = ctrabalho = int(input('Informe o número da CTPS: (0 caso não tenha)'))
hoje = int(datetime.date.today().year)
idade = hoje - datanas
dados['idade'] = idade
if ctrabalho != 0:
    dados['contratação'] = anocont = int(input('Digite o Ano da contratação: [0000]'))
    dados['dados'] = salario = float(input('Digite o salário: '))
    tempor = 35 - (hoje - anocont)
    dados['aposentadoria'] = aposenta = idade + tempor
for k, v in dados.items():
    print(f'---> {k} tem valor {v}')