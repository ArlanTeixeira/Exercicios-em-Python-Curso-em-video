def moeda(preço=0):
     return f'R${preço:.2f}'


def aumentar(v=0, a=0, p=0):
    nv = v + (v * a / 100)
    if p == True:
        return f'R${nv:.2f}'
    else:
        return nv


def diminuir(v, a, p):
    nv = v - (v * a/100)
    if p == True:
        return f'R${nv:.2f}'
    else:
        return nv


def metade (v, p):
    if p == True:
        return f'R${v/2:.2f}'
    else:
        return v/2



def dobro (v, p):
    if p == True:
        return f'R${v*2:.2f}'
    else:
        return v * 2


def resumo(p=10, txAumento=10, txReducao=5):
    print('-' *30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Analisando o valor: \t{moeda(p)}')
    print(f'Dobro do preço: \t{dobro(p, True)}')
    print(f'Metade do preço: \t{metade(p, True)}')
    print(f'Com o aumento de {txAumento}% o novo valor é de \t{aumentar(p, txAumento, True)}')
    print(f'Com a redução de{txReducao}% o novo valor é de \t{diminuir(p,txReducao, True)}')


