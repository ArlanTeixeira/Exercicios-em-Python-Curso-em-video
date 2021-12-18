gols= list()
totgols = 0
jogador = str(input('Digite o nome do Jogador: '))
jogos = int(input(f'Quantos jogos o {jogador} jogou: '))
for c in range(0, jogos):
    gol = int(input(f'Quantos gols {jogador} marcou na partida {c +1}: '))
    totgols += gol
    gols.append(gol)
dados = {'nome': jogador, 'gols': gols, 'total gols': totgols}
for k, v in dados.items():
    print(f'O campo {k} tem o valor  de:  {v}')
print(f'O jogaor {jogador} jogou {jogos} partidas')
for c in range(0, jogos):
   print(f'Na partida {c + 1},ele fez {gols[c]} gols ')
print(f'Foi um total de: {dados["total gols"]} gols')
