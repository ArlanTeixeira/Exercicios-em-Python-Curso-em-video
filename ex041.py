import datetime
ano = int(input('Insira o ano de nascimento do aluno: '))
idade = datetime.date.today().year - ano

if idade > 0 and idade <= 9:
    print('O aluno tem {} anos e está na categoria Mirim'.format(idade))
elif idade > 9 and idade <= 14:
    print('O aluno tem {} anos e está na categoria Infantil'.format(idade))
elif idade > 14 and idade <=19:
    print('O aluno tem {} anos e está na categoria Junior'.format(idade))
elif idade == 20:
    print('O aluno tem {} anos e está na categoria Senior'.format(idade))
elif idade > 25:
    print('O aluno tem {} anos e está na categoria Master'.format(idade))