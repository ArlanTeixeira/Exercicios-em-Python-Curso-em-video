totalg = 0
menos = 0
nomebarato = ''
contp = 1
menor = 0
print('Loja Baratão da Informática')
while True:
    nomep = str(input('Digite o nome do Produto: '))
    preçop = float(input(('Digite o Preço do Produto:')))
    totalg += preçop
    if preçop < 1000:
        menos += 1
    if contp == 1:
        menor = preçop
        nomebarato = nomep
    else:
        if preçop < menor:
            menor = preçop
            nomebarato = nomep
    r = ' '
    while r not in 'SN':
        r = str(input('Deseja continuar:[S,N] ')).upper().strip()[0]
    if r == 'N':
        break
print(f'O total da compra foi de R${totalg:.2f}')
print(f'Temos {menos} produtos custando menos de R$ 1000,00')
print(f'O produto mais barato foi {nomebarato} que custa R${menor:.2f}')