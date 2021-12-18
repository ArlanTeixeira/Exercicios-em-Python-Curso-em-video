import math
num1 = float(input('Insira o valor do cateto oposto: '))
num2 = float(input('Insira o valor do cateto adjascente: '))
hipotenusa = math.hypot(num1, num2)
print('O valor da hipotenusa é: {}'.format(hipotenusa))
