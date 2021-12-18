maior18 = 0
homens = 0
mulher20 = 0
while True:
    print('======== CADASTRO DE PESSOAS =======')
    idade = int(input('Digite a idade da Pessoa: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo da Pessoa: [M/F] ')).upper().strip()[0]
    if idade > 18:
        maior18 += 1
    if sexo in 'Mm':
        homens += 1
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1
    r = ' '
    while r not in 'SN':
        r = str(input('Deseja continuar? [S/N]: ')).upper().strip()
    if r == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maior18}')
print(f'Total de homens cadastrados: {homens}')
print(f'Total de mulheres com menos de 20 anos: {mulher20}')
