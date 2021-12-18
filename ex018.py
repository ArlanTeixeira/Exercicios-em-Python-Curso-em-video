import math
angulo= float(input('Insira o agulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O agunlo {} tem como seno {:.2f}, como cosseno {:.2f} e como tangente {:.2f}'.format(
    angulo, seno, cosseno, tangente
))

