valores = []
maior = 0
menor = 0
for v in range(0,5):
    valores.append(int(input(f'Insira um Valor na posição {v}: ')))
    if v == 0:
        maior = menor = valores[v]
    else:
        if valores[v] > maior:
         maior = valores[v]
        if valores[v] < menor:
            menor = valores[v]
print(f'O maior valor foi {maior} na posição ', end=' ')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end=' ')
print(f'\nO menor valor foi {menor} na posição ', end=' ')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end=' ')

