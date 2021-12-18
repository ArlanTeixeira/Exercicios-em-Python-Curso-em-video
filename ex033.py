n1 = int(input("Escreva o primeiro número: "))
n2 = int(input("Escreva o segundo  número: "))
n3 = int(input("Escreva o terceiro número: "))

if n1 > n2 and n1 > n3:
    print('O primeiro número {} é o maior'.format(n1))
elif n2 > n1 and n2 > n3:
    print('O segundo número {} é o maior'.format(n2))
elif n3 > n1 and n3 > n2:
    print('O terceiro número {} é o maior'.format(n3))
if n1 < n2 and n1 < n3:
    print('O primeiro número {} é o menor'.format(n1))
elif n2 < n1 and n2 < n3:
    print('O segundo número {} é o menor'.format(n2))
elif n3 < n1 and n3 < n2:
    print('O terceiro número {} é o menor'.format(n3))



