listagem = ('Lápis', 1.75,
            'Caneta', 2.50,
            'Apontador', 1.50,
            'Estojo', 5.00,
            'Cola', 3.75,
            'Mochila', 42.90,
            'Caderno', 15.99,
            'Livos', 345.60,
            'Borracha', 0.90)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')
print('-' * 40)

