'''teste = list()
teste.append('Arlan')
teste.append(32)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 25
galera.append(teste[:])
print(galera)
galera = [['Arlan', 32], ['Dino', 33], ['Aécio', 35], ['Walter', 48]]
for p in galera:
    print(f'Nome: {p[0]:<}', end=' ')
    print(f'Idade: {p[1]}')'''
galera = list()
dado = list()
totmai = totmen = 0
for p in range(0,3):
    dado.append(str(input('Digite o nome da Pessoa: ')))
    dado.append(int(input('Insira a Idade da Pessoa: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
for p in galera:
    if p[1] > 18:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Existem {totmai} maiores de idade e {totmen} menores de idade')
