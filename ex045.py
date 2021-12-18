import random
from time import sleep
print('Bem vindo ao Jogo Jokenpo')
print('_' *40)
j = str(input('Qual sua escolha: pedra, papel ou tesoura? \n'))
print('Você escolheu {}'.format(j))
lista = ['pedra', 'papel', 'tesoura']
pc = random.choice(lista)
print('o computador escolheu... {}'.format(pc))
print('gerando resultado \n', '*' *40)
sleep(2)
if j == 'pedra' and pc == 'pedra':
    print('O jogo deu empate!')
elif j == 'pedra' and pc == 'tesoura':
    print('Você venceu o jogo!')
elif j == 'pedra' and pc == 'papel':
    print('O computador venceu o jogo!')
elif j == 'tesoura' and pc == 'tesoura':
    print('O jogo deu empate!')
elif j == 'tesoura' and pc == 'papel':
    print('Você venceu o jogo!')
elif j == 'tesoura' and pc == 'pedra':
    print('O computador venceu o jogo!')
elif j == 'papel' and pc == 'papel':
    print('O jogo deu empate!')
elif j == 'papel' and pc == 'pedra':
    print('Você venceu o jogo!')
elif j == 'papel' and pc == 'tesoura':
    print('O computador venceu o jogo!')



