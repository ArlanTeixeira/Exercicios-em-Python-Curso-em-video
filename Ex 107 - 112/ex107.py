import moeda
p = float(input('Digite um valor: '))
print(f'Aumentando {p} em 10% temos: {moeda.aumentar(p, 10)}')
print(f'Diminuindo {p} em 13% temos: {moeda.diminuir(p, 13)}')
print(f'O dobro de {p} é: {moeda.dobro(p)}')
print(f'A metade de {p} é: {moeda.metade(p)}')