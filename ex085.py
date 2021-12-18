listaNum = list ()
listaNumPar = list ()
listaNumImpar = list()
for c in range(0, 7):
    listaNum.append(int(input(f'Digite o {c + 1}º número: ')))
for n in listaNum:
    if n % 2 == 0:
        listaNumPar.append(n)
    else:
        listaNumImpar.append(n)
print(listaNum)
print(f'Os valores pares digitados foram: {sorted(listaNumPar)}')
print(f'Os valores impares digitados foram: {sorted(listaNumImpar)}')
