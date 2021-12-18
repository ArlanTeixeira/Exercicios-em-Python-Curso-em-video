sexo = str(input('Digite o sexo da pessoa: [M/F]')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválios. Digite o sexo da pessoa: [M/F]')).strip().upper()[0]
print('Sexo {}, registrado com sucesso!'.format(sexo))
