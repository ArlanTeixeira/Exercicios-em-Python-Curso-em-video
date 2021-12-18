# minha solução
'''n = int(input('Digite um número: '))
resultado=1
count=1
while count <= n:
    print('{}'.format(count), end='')
    print(' x ' if count < n else ' = ', end='')
    resultado *= count
    count += 1
print('{}'.format(resultado))
print('Fim do programa!')'''
# Solução Guanabara
n = int(input('Digite um número: '))
cont = n
resultado = 1
print('O fatorial de {}! é'.format(n))
while cont > 0:
    print('{}'.format(cont), end='')
    print(' x ' if cont > 1 else ' = ', end='')
    resultado *= cont
    cont -= 1
print('{}'.format(resultado))
