def fatorial(n, show = False):
    """
    -> Calcula o fatorial de um número.
    :param n: O número a ser calculado.
    :param show: Mostrar ou não a conta.
    :return: o valor do fatorial do número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(f'{c}',end=' ')
            print('x' if c > 1 else '=', end=' ')
        f *= c
    return f # Este return deverá ser fora do laço 'for' para funcionar corretamente


print(fatorial(5, show = True))
help(fatorial)
