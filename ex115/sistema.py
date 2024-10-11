from ex115.lib.interface import * # ESte comando de 'import *' serve para importar tudo
from ex115.lib.arquivo import *

arquivo = 'CursoemVideo.txt' # Variável criada para usar em diversos momentos de teste

if not arquivoexiste(arquivo):
    criararquivo(arquivo)


while True:
    resposta = menu(['LISTA DE PESSOAS', 'CADASTRAR PESSOA', 'SAIR DO SISTEMA'])
    if resposta == 1:
        lerarquivo(arquivo)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('NOME: '))
        idade = leiaint('IDADE: ')
        cadastrar(arquivo, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema...')
        break
    else:
        cabeçalho('\033[31mErro! Digite uma opção válida.\033[m')
