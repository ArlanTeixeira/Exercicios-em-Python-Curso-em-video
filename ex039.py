import datetime
nascimento = int(input('Insira o ano de nascimento: '))
idade = datetime.date.today().year - nascimento
if idade < 18:
    print('Você tem {} anos e ainda vai se alistar ás forças armadas!'.format(idade))
elif idade == 18:
    print('Você tem 18 anos e deve se alistar ás forças armadas!')
else:
    print('Você tem {} anos e já não precisa mais se alistar'.format(idade))


