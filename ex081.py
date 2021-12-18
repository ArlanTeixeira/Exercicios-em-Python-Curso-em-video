lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    r = str(input('Deseja Continuar? '))
    if r in 'Nn':
        break
print(f'Foram digitados {len(lista)} valores')
lista.sort(reverse=True)
print(f'A ordem decrescente dos valores é {lista}')
if 5 in lista:
    print('O número 5 está na Lista')
else:
    print('O valor 5 não está na lista')
