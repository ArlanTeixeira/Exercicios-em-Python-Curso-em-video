n1 = float(input('Insira a primeira nota'))
n2 = float(input('Insira a segunda nota'))
media = (n1 + n2) /2
if media < 5:
    print('Sua note média é {:.1f} e você está reprovado!'.format(media))
elif media >= 5 and media < 7:
    print('Sua média é {:.1f} e você está de recuperação '.format(media))
else:
    print('Sua média é de {:.1f} e você está aprovado!'.format(media))
