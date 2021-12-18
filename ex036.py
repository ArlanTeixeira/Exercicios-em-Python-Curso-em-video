valorcasa = float(input('Digite o valor do imóvel: '))
salario = float(input('Digite o valor do sálario do solicitante: '))
tempo = int(input('Digite em quantos anos o solicitante pretende pagar o imóvel: '))

np = tempo * 12
prestacao = valorcasa/np

if prestacao > salario * 0.30:
    print('Emprésto negado! O valor da prestação {:.2f} excede mais do que 30% seu salário'
          .format(prestacao))
else:
    print('Empréstimo aprovado! O valor da sua prestção é de: {:.2f}'.format(prestacao))