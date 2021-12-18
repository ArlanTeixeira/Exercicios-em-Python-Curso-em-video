s1 = float(input('Digite o primeiro seguimento: '))
s2 = float(input('Digite o segundo seguimento: '))
s3 = float(input('Digite o terceiro seguimento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos aciam podem formar um triangulo')
else:
    print('Os seguimento acima não podem formar um triagunlo')



