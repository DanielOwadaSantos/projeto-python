lista = 'lapis', 1.00,\
    'borracha', 0.50,\
    'caneta', 1.50
print('-'*40)
print(f'{"LISTA DE PREÇOS":^40}')# coloque a string em aspas duplas para formatar e não afetar a impressão
                                 # ':^40' siginifica alinhado ao centro em 40 posições
print('-'*40)
for pos in range(0, len(lista)):#Use este método para mostrar os itens em forma de tabela .
    if pos %2==0:# se for par mostra os produtos, se for impar mostra os preços(%2==1)
        print(f'{lista[pos]:.<30}',end='')#':.<'siginifica alinhado à esquerda com pontinhos,30 é quantidade de caracteres
                                          #',end='' é a quebra de linha somente nos preços
    else:
        print(f'R${lista[pos]:>7.2f}')# '>7' significa alinhado à direita depois do R$ com 7 posições
                                      # '.2f' siginifica que o preço está com duas casas decimais
print('-'*40)