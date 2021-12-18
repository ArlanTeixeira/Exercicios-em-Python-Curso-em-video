v = float(input('Informe a velocidade do carro: '))
vm = 80.0
if v > vm:
    print('Você ultrapassou o limite de velocidade e foi multado!')
    cm = (v - vm) * 7
    print('O valor da sua multa foi de {:.2f}'.format(cm))
else:
    print('Seu carro está dentro da velocidade permitida na via')

