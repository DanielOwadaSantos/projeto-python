def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(TypeError,ValueError):
            print('\033[31mErro. Digite um número válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\033[31mPrograma interrompido.\033[m')
            return 0
        else:
            return n



def linha(tam=42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42)) # Este comando serve para centralizar seu texto e o número 42 foi pré definido anteriormente
    print(linha())


def menu(lista):
    cabeçalho('MENU PRINCIPAL') # Observa que são feitas chamadas dentro de outras sem ocorrer erros
    c = 1 # Este 'c' para criar a numeração do menu
    for item in lista: # Looping para colocar os itens da lista da pasta sistema
        print(f'\033[32m{c}-\033[34m{item}') # Print para mostrar o menu interativo
        c += 1 # Aqui vai se somando quantos items tem no menu
    print(linha())
    opc = leiaint('\33[32mSua Opção: \033[m')
    return opc
    