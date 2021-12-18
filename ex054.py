import datetime
menor = 0
maior = 0
for c in range(1, 8):
    ano = int(input('Escreve o nascimento da {}° Pessoa: '.format(c)))
    if datetime.date.today().year - ano >= 18:
        maior += 1
    else:
        menor += 1
print('Existem {} pessoas maiores de idade.'.format(maior))
print('E {} sãoo menores de idade'.format(menor))
