def aumentar(preço=0, taxa=0, formato=False):
    '''
    -> Calcula o aumento de um determindado preço,
    retornando o resultado com ou sem formatação
    :param preço: O preço que se quer reajustar
    :param taxa: Qual a porcentagem do aumento
    :param formato: Quer a saída formatada ou não
    :return: O valor reajustado com ou sem formato
    '''
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if formato is False else moeda(res)


def metade(preço=0, formato=False):
    res = preço / 2
    return res if formato is False else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>6.2f}'.replace('.',',')


def resumo(preco=0, taxaa=10, taxar=5):
    print('-' * 30)
    print(f'RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Analisando o valor: \t{moeda(preco)}')
    print(f'O dobro de {moeda(preco)}: \t{dobro(preco, True)}')
    print(f'A metade de {moeda(preco)}: \t{metade(preco, True)}')
    print(f'{taxaa}% de aumento: \t\t{aumentar(preco, taxaa, True)}')
    print(f'{taxar}% de desconto: \t\t{diminuir(preco, taxar, True)}')
    print('-' * 30)
