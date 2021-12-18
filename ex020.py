import random
aluno1 = input('Insira o nome do Aluno 1: ')
aluno2 = input('Insira o nome do Aluno 2: ')
aluno3 = input('Insira o nome do Aluno 3: ')
aluno4 = input('Insira o nome do Aluno 4: ')
lista = [aluno1,aluno2,aluno3,aluno4]
random.shuffle(lista)
print('A orde de apresentação será: ', lista)

