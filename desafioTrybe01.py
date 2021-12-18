def converteTemperatura(temperatura, escalaOrigem, escalaDesejada):
    # Write your code here
    if escalaOrigem == escalaDesejada:
        print("Você deve informar duas escalas diferentes")
    else:
        if escalaOrigem == 'celsius' and escalaDesejada == 'fahrenheit':
            temperaturaC = (temperatura * 1.8) + 32
        elif escalaOrigem == 'celsius' and escalaDesejada == 'kelvin':
            temperaturaC = temperatura + 273.15
        elif escalaOrigem == 'fahrenheit' and escalaDesejada == 'celsius':
            temperaturaC = (temperatura - 32) / 1.8
        elif escalaOrigem == 'kelvin' and escalaDesejada == 'celsius':
            temperaturaC = temperatura - 273.15
    print(temperaturaC)

converteTemperatura(2, 'celsius', 'fahrenheit')

