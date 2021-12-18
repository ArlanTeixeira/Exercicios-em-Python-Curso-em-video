import moeda

p = float(input('Digite um valor: '))
print(f'Aumentando {p} em 10% temos: {moeda.aumentar(p, 10, True)}')
print(f'Diminuindo {p} em 13% temos: {moeda.diminuir(p, 13, True)}')
print(f'O dobro de {p} é: {moeda.dobro(p, True)}')
print(f'A metade de {p} é: {moeda.metade(p, True)}')

print('-' * 10, 'PRINT SEM FORMATAÇÃO', '-' * 10)

print(f'Aumentando {p} em 10% temos: {moeda.aumentar(p, 10, False)}')
print(f'Diminuindo {p} em 13% temos: {moeda.diminuir(p, 13, False)}')
print(f'O dobro de {p} é: {moeda.dobro(p, False)}')
print(f'A metade de {p} é: {moeda.metade(p, False)}')