from time import sleep
n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))
e = 0
while e != 5:
    print(' [1]Somar \n [2]Multiplicar \n [3]Maior \n [4]Novos Números \n [5]Sair do Programa')
    e = int(input('>>>>>> Qual a sua opção: <<<<<<<\n'))
    if e == 1:
        print('A soma dos dois valores é: {}'.format(n1 + n2))
    elif e == 2:
        print('A multiplicação dos valores é igual a {}'.format(n1 * n2))
    elif e == 3:
        if n1 > n2:
            print('O primeiro valor é o maior!')
        if n1 < n2:
            print('O segundo valor é o maior!')
        else:
            print('Os valores são iguais')
    elif e == 4:
        print('Digite os novos valores')
        n1 = float(input('Digite o primeiro valor: '))
        n2 = float(input('Digite o segundo valor: '))
    elif e == 5:
        print('O programa será encerrado...')

    else:
        print('Opcção inválida')
    print('=-=' * 12)
    sleep(1.5)
print('Programa encerrado!')
