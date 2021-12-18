# Resolução com o For
'''
pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razaão da PA: '))
décimo = pt + (10 - 1) * r
for c in range(pt, décimo + r,  r):
    print('{}'.format(c), end='-> ')
    '''
# Resolução com while
pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razaão da PA: '))
termo = pt
c = 1
resultado = 1
while c <= 10:
    print('{} -> '.format(termo), end='')
    termo += r
    c += 1
print('FIM')
