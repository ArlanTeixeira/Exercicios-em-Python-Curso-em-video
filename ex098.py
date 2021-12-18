from time import sleep

def contador(i, f, p):
    print(f' Contando de {i} até {f} de {p} em {p}')
    if p < 0:
        p *= -1
    if p == 0:
        p = 1

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end="")
            sleep(0.3)
            cont += p
        print('FIM!')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end="")
            sleep(0.3)
            cont -= p
        print('FIM')


contador(50, 0, 5)
contador(10, 40, 3)
print("Agora você quem escolho o ÍNICIO, o FIM, e o PASSO")
ini = int(input('Escreva o ÍNICIO: '))
fim = int(input('Escreva o FIM:    '))
passo = int(input('Escreva o PASSO: '))
contador(ini, fim, passo)
