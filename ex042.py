s1 = float(input('Digite o primeiro seguimento: '))
s2 = float(input('Digite o segundo seguimento: '))
s3 = float(input('Digite o terceiro seguimento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos aciam podem formar um triangulo')
    if s1 == s2 and s1 == s3 and s2 == s3:
        print('Seu triângulo é Equilatero, todos lados são iguais')
    elif s1 == s2 or s1 == s3 or s2 == s3 :
        print('Seu triângulo é Isoceles, possui dois lados iguais')
    elif s1 != s2 and s1 != s3 and s2!= s3:
        print('Seu triângulo é Escaleno, todos os lador diferentes')
else:
    print('Os seguimento acima não podem formar um triagunlo')