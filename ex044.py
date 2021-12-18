preço = float(input('Informe o preço do produto: '))
fp = int(input('Agora informe a forma de pagamento sendo: \n'
               '1 para Dinheiro \n'
               '2 para à vista no cartão \n'
               '3 para 2x no cartão \n'
               '4 para 3x no cartão \n'
               '_______________________ \n'))
if fp == 1:
    preço = preço - (preço * 0.10)
    print('Você escolheu dinheiro como forma de pagamento \n'
          'Você recebeu um desconto de 10% e agora o produto custa {}'.format(preço))
elif fp == 2:
    preço = preço - (preço * 0.05)
    print('Você escolheu à vista no cartão como forma de pagamento \n'
          'Você recebeu um desconto de 5% e agora o produto custa {}'.format(preço))
elif fp == 3:
    print('Você escolheu dividir o pagamento em 2x no cartão \n'
          'O produto não terá alteração de preço: {}'.format(preço))
elif fp == 4:
    preço = preço + (preço * 0.20)
    print('Você escolheu dividir o pagamento em 3x \n'
          'O preço do produto será acrescido em 20% {}'.format(preço))
else:
    print('Forma de pagamento inexistente. Tente novamente')
        





