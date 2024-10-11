from ex115.lib.interface import *
# FUNCÃO QUE VERIFICA SE O ARQUIVO EXISTE

def arquivoexiste(nome): # Aqui está recebendo o nome do aquivo criado 'cursoemvideo'
    try: # Use tratamentop de erro para verificação de arquivo
        a = open(nome, 'rt') # Aqui estamos usando a variavel 'cursoemvideo' para  verificação de aqruivo
        a.close() # Função open para abrir arquivo e close para fechar, 'rt' signofca read text, ler texto
    except FileNotFoundError: # exeção para verificar se arquivo existe
        return False # se o arquivo não existir retorne false
    else:
        return True # Se existir retorne true


# FUNÇÃO QUE CRIA O ARQUIVO INEXISTENTE


def criararquivo(nome):
    try:
        a = open(nome, 'wt+') # Este 'wt+' sigifica write text, ou seja, será criada um arquivo novo graças ao '+'
        a.close()
    except:
        print('Houve um erro na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


# FUNÇÃO PARA MOSTRAR ARQUIVO FORMATADO
def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Não foi possível abrir o arquivo')
    else:
        cabeçalho('Lista de pessoas:') # Para usar o cabeçalho faça importação de ex115
        for linha in a: # Para cada linha in arquivo:
            dado = linha.split(';') # Foi criado dado e splitado por ';' como feito anteriormente
            dado[1] = dado[1].replace('\n','') # Aqui trocamos a linha vazia por nada
            print(f'{dado[0]:<30}{dado[1]:>3} anos') # Por ter '\n' nativo no arq. txt e outro na função cadastrar, teremos
                                    # uma linha em branco, para isto faça o passo acima
    finally:
        a.close()


# FUNÇÃO PARA CADASTRO DE NOVAS PESSOAS
def cadastrar(arquivo, nome='desconhecido', idade=0):
    try:
        a = open(arquivo, 'at') # Aqui 'at' significa append text, para adicionar pessoa ao arquivo txt
    except:
        print('Houve um erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro no cadastro!')
        else:
            print('Novo registro adicionado com sucesso!')
            a.close()