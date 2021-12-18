frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
'''for letra in range (len(junto) - 1, -1, -1):
    inverso += junto[letra]''' # este é o modo mais extenso!
print('O inverso de {} é {}'.format(junto, inverso))
if junto == inverso:
    print('Temos um pálindromo')
else:
    print('A frase digitada não é um pálindromo')


