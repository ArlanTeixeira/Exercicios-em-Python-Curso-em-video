import random
palpites = 0
acertou = False
n = random.randint(0, 10)
while not acertou:
    nu = int(input('Escreva um número: '))
    palpites +=1
    if n == nu:
        acertou = True
    else:
        if nu < n:
            print('Mais... Tente novamente!')
        elif nu > n:
            print('Menos... Tente Novamente')

print('Você precisou de {} tentativas para acertar'.format(palpites))
