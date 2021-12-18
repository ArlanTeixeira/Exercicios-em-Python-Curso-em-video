cont = 1
soma = 0
media = 0
maior = 0
menor = 0
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Deseja continuar: [S/N]')).upper()
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    cont += 1
    soma = soma + n
media = soma/cont
print('Você digitou {} números, a média entre ele foi {:.2f} \n O maior número foi {}'
      ' e o menor número foi {}'.format(cont, media, maior, menor))


