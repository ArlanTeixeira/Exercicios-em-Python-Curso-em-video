from ex115.Lib.Interface import *
from ex115.Lib.arquivo import *
arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Listar Pessoas', 'Cadastrar Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # Leitura do arquivo
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Digite no nome: '))
        idade = leiaInt('Informe a idade: ')
        cadastrar(arq, nome, idade)


    elif resposta == 3:
        cabeçalho('Saindo do Sistema...')
        break
    else:
        print('ERRO! Digite uma opção válida')
