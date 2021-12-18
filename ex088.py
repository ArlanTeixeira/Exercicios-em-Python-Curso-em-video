import random
import time
grupoJogo = list()
jogo = list()
jogos = int(input('Digite quantos Jogos você vai querer: '))
print('=' * 20, f'Sorteando {jogos} jogos', '=' * 20)
for j in range(0, jogos):
    jogo.append(random.sample(range(1, 61), 6))
    time.sleep(1)
    grupoJogo = jogo[:]

for j in range(0, jogos):
    grupoJogo.sort()
    print(f'Resultado jogo {j+1}: {grupoJogo}')
