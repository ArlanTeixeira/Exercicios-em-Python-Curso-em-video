lista = []
listapar = []
listaimpar = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)
    r = str(input('Deseja continuar?'))
    if r in 'Nn':
        break
print(f'Os números digitados foram: {lista}')
print(f'Os números pares são: {listapar}')
print(f'Os números impares são: {listaimpar}')
