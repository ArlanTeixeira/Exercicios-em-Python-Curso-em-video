pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razaão da PA: '))
décimo = pt + (10 - 1) * r
for c in range(pt, décimo + r,  r):
    if c > décimo - 1:
        print(f'{c}', end="")
    else:
        print('{}'.format(c), end='-> ')