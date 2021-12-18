
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = 0
contmulher = 0
for c in range(1, 5):
    print('----- {}° PESSOA ------'.format(c))
    nome = str(input('Escreva o nome da pessoa: ')).strip()
    idade = int(input('Escreva a idade da pessoa: '))
    sexo = str(input('Informe o sexo [M/F]: ')).strip()
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        contmulher += 1

mediaidade = somaidade / 4
print('A média das idades do grupo é {}'.format(mediaidade))
print('{} é o homem mais velho com {} anos'.format(nomevelho, maioridadehomem))
print('Existem {} mulheres com menos de 20 anos'.format(contmulher))