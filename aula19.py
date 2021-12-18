estado = dict()
brasil = list()
for c in range(0,3):
    estado['uf'] = str(input('Digite o nome do Estado: '))
    estado['sigla'] = str(input('Digite a sigla do Estado: '))
    brasil.append(estado.copy())
for p in brasil:
    print(f'Nome do Estado:{p["uf"]}. sigla do Estado: {p["sigla"]}')
