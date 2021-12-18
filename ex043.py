peso = float(input('Insira o peso: '))
altura = float(input('Insira a altura da pessoa em metros: '))
IMC = peso / (altura ** 2)
if IMC < 18.5:
    print('Seu IMC é {} e você está abaixo do peso'.format(IMC))
elif IMC >= 18.5 and IMC < 25:
    print('Seu IMC é {} e você está no peso ideal'.format(IMC))
elif IMC >= 25 and IMC < 30:
    print('Seu IMC é {} e você está com sobrepeso'.format(IMC))
elif IMC >= 30 and IMC < 40:
    print('Seu IMC é  {} e você está obeso'.format(IMC))
elif IMC >= 40:
    print('Seu IMC é {} e você está com obesidade morbida'.format(IMC))
