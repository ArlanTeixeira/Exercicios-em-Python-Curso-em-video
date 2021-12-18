n = 0
cont = 0
soma = 0
while n != 999:
    n = int(input('Escreva um número ou 999 para encerrar: '))
    if n != 999:
        soma += + n
        cont += 1
print('Progama encerrado!')
print('você escreveu {} números e a soma deles é {}'.format(cont, soma))
