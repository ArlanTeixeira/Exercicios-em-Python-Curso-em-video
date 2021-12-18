'''num = [1, 5, 2, 7]
print(num)
num.append(9)
num.sort()
print(num)
num.sort()
num.sort(reverse=True)
print(num)
print(f'Essa função possui {len(num)} elementos')
num.insert(2,0)
print(num)
num.pop(2)
print(num)'''

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for v in valores:
    print(f'{v}...')
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
for cont in range(0,5):
    valores.append(int(input('Digite um Valor: ')))
print(valores)

