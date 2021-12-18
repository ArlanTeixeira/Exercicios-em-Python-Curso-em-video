v1 = int(input('Insira o primeiro valor: '))
v2 = int(input('Insira o segundo valor: '))

if v1 > v2:
    print('O primeiro valor {} é maior que o segundo {}'.format(v1, v2))
elif v2 > v1:
    print('O segundo valor {} é maior que o primeiro valor {}'.format(v2, v1))
else:
    print('Os dois valores são iguais!')

