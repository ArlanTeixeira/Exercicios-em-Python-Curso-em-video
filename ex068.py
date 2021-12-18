import random
print('-=-' * 15)
print('JOGO PAR OU IMPAR')
print('-=-' * 15)
contv = 0
while True:
    nj = int(input('Escolha seu número: '))
    nc = random.randint(0, 11)
    total = nj + nc
    ej = ' '
    while ej not in 'PI':
        ej = str(input('Você Escolhe par ou impar: [P/I]')).strip().upper()[0]
    print(f'Voce jogou {nj} e o computador {nc}. O total é {nj + nc}')
    if ej == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            contv += 1
        else:
            print('Você Perdeu!')
            break
    elif ej == 'I':
        if total % 2 != 0:
            print('Você venceu!')
            contv += 1
        else:
            print('Você Perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'Jogo encerrado. Você venceu {contv} vezes')

