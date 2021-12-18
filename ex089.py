ficha = list()
while True:
    nome = str(input('Digite o nome do aluno: '))
    nota1 = float((input('Digite a primeira nota: ')))
    nota2 = float((input('Digite a segunda nota: ')))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    r = str(input('Deseja continuar? [S/N]'))
    if r in 'Nn':
        break
print('=' * 30)
print(f'{"NO.":<4}{"NOME":^10}{"MÉDIA":>8}')
print('-' * 30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:^10}{a[2]:>8.1f}')
while True:
    opc = int(input('Você deseja ver as notas de qual aluno?: [999] para encerrar'))
    if opc == 999:
        print('Finalizando programa...')
        break
    if opc <= len(ficha) -1:
        print(f'As notas do aluno {ficha[opc][0]} são: {ficha[opc][1]}')
print('<<<< FIM DO PROGRAMA >>>>')


