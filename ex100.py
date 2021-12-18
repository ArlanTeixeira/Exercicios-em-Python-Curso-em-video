from random import randint


def sorteia(lista):
    print('Sorteando números...')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end="")
    print('\nPRONTO!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor %2 == 0:
            soma += valor
    print(f'Analisando os valores pares de {lista}, temos a soma de {soma}')


numeros = list()
sorteia(numeros)
somaPar(numeros)
