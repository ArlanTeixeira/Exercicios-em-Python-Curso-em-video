pt = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razaão da PA: '))
termo = pt
ct = 10
c = 1
resultado = 1
while c <= 10:
    print('{} ->'.format(termo), end='')
    termo += r
    c += 1
    if c > 10:
        print('\n Deseja exibir mais termos? Digite 0 para encerar')
        n = int(input('Digite quantos temos a mais você deseja ver: '))
        ct = ct + n
        if n != 0:
            c -= n
print('Progreção finalizada com {} termos mostrados'.format(ct))
