cont = 0
print('-' * 20)
while True:
    n = int(input('de qual número você quer saber a tabuada: '))
    if n < 0:
        break
    cont = 1
    while cont < 10:
        cont += 1
        print(f'{n} x {cont} = {n * cont}')
print('Fim do programa')
