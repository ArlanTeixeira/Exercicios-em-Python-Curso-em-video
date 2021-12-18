time = list()
gols= list()
jogador = dict()
totgols = 0
while True:
    jogador.clear
    jogador['nome'] = str(input('Digite o nome do Jogador: '))
    jogos = int(input(f'Quantos jogos o {jogador["nome"]} jogou: '))
    gols.clear()
    for c in range(0, jogos):
        gol = int(input(f'Quantos gols {jogador["nome"]} marcou na partida {c +1}: '))
        totgols += gol
        gols.append(gol)
        gols.clear()
    dados = {'nome': jogador, 'gols': gols, 'total gols': totgols}
    while True:
        resp = str(input('Deseja continuar: [S/N]')).upper()[0]
        if resp in "SN":
            break
        print('Erro! Digite apenas S OU N')
    if resp == 'N':
        break
for k, v in dados.items():
    print(f'O campo {k} tem o valor  de:  {v}')
print(f'O jogador {jogador} jogou {jogos} partidas')
for c in range(0, jogos):
   print(f'Na partida {c + 1},ele fez {gols[c]} gols ')
print(f'Foi um total de: {dados["total gols"]} gols')