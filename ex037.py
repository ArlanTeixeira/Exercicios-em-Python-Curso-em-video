n1 = int(input('digite um número inteiro: '))
print(''' Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] conerter para Hexadecimal''')
opcao = int(input('Sua opcção: '))

if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(n1, bin(n1)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(n1, oct(n1)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igua a {}'.format(n1, hex(n1)[2:]))
else:
    print('Opção Inválilda!')
