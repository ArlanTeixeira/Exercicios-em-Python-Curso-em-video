valores = []
while True:
    n = int(input('Escreva um número: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com Sucesso')
    else:
        print('Valor Duplicado e não será adicionado a lista')
    r = str(input('Deseja continuar?'))
    if r in 'Nn':
        break
print('-=' * 30)
print(f'Você digitou os valores {sorted(valores)}')