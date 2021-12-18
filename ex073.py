tabelaBrasileiro = ('Flamengo', 'Palmeiras', 'Internacional', 'São Paulo', 'Fluminense', 'Santos',
                    'Grêmio', 'Atlétio PR', 'Atlético Mineiro', 'Bragantino', 'Bahia', 'Chapecoense',
                    'Fortaleza', 'Ceará', 'Corinthians', 'Sport', 'Atlétigo GO', 'Vasco', 'Goiás',
                    'Coritiba', 'Botafogo')
print(f'Os cinco primeiro colocados são: {tabelaBrasileiro[:5]}')
print(f'Os quatro times rabaixados para a série B são: {tabelaBrasileiro[-4:]}')
print(f'Os times em ordem alfabética são: {sorted(tabelaBrasileiro)}')
print(f'A Chapecoence está na {tabelaBrasileiro.index("Chapecoense")+1}ª colocação')

