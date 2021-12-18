num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez'
       'onze', 'doze', 'treze', 'cartoze', 'quinze', 'dezessei', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        break
    erro = int(input('Opcão Inválida. Tente novamente: '))
print(f'Você digitou o número {num[n]}')
r = str(input('Você deseja continuar? [S/N]')).strip().upper()
while 'S' in r:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        break
    erro = int(input('Opcão Inválida. Tente novamente: '))
print(f'Você digitou o número {num[n]}')
