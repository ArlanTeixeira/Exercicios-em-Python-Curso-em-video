import random
from time import sleep
n = random.randint(0,5)
nu = int(input('Escreva um número: '))
print('Processando...')
sleep(3)
if n == nu:
    print('O número do computador foi {} e o seu foi {}, Parabens, você venceu!'
          .format(n, nu))
else:
    print('O número do computador foi {} e o seu foi {}, que pena, você perdeu!'
          .format(n, nu))
