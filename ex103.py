def ficha(nome='desconhecido', gols=0):
    print(f'O jogador {nome} fez {gols} no campeonato!')

n = str(input('Escreva o nome do Jogador: '))
g = str(input('Quantos gols fez: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
