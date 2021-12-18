a = int(input('Digite o 1° número: '))
b = int(input('Digite o 2° número: '))
c = int(input('Digite o 3° número:  '))
d = int(input('Digite o 4° número: '))
n = (a, b, c, d)
print(f'Os seguintes valores foram digitados: {n}')

if 9 in n:
     print(f'O número 9 apareceu {n.count(9)} vezes')
else:
     print('Não houve ocorrência do número 9')
if 3 in n:
    print(f'O número 3 apareceu na {n.index(3)+ 1}ª posição')
else:
    print('O número 3 não foi digitado')
for nc in n:
    if nc % 2 == 0:
     print(f'Os seguintes números são pares: {nc}')


