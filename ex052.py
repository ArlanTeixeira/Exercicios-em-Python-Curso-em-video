n = int(input('Diga o número: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[31m', end=' ')
        tot += 1
    else:
        print('\033[m', end=' ')
    print('{}'.format(c), end=' ')
print('\n \033[mO número {} foi divisível {} vezes'.format(n, tot))
if tot == 2:
    print('Portanto ele é um número primo')
else:
    print('Portanto não é um número primo')
