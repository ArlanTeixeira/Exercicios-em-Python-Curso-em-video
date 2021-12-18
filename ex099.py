def maior(* num):
    cont = maior = 0
    print('\nAnalisando os valores...')
    for valor in num:
        print(f'{valor} ', end="")
        if cont == 1:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam analisados {cont} valores')
    print(f'E o maior deles é {maior}')
maior(8, 3, 9, 4, 2, 0)
maior(4, 7, 0)
#maior(1, 2)
#maior(0)