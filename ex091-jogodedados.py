from random import randint
from time import sleep
from operator import itemgetter # Use a função 'itemgetter' para ordenar elementos na posição 1,
                            # neste caso das posições randint
jogo = {'Jogador 1': randint(1,6),
        'Jogador 2': randint(1,6),
        'Jogador 3': randint(1,6),
        'Jogador 4': randint(1,6)}
ranking = {} # Aquin neste caso poderia ser tambem list(), ranking = ()
print(f'{"VALORES SORTEADOS NO DADO":=^30}')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(0.5)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse= True) # Aqui está ordenado usando a função sorted, porém será
                                        # oredenado pela posição 1 pois está com a função da 'key' itemgetter(1), ou
                                        # seja, será ordenado pelos valores, se fosse itemgetter(0) seria ordenado pela
                                        # posição 0 ou seja pelas chaves
                                        # Use estes codigos na mesma linha pois irão representar neste caso o 'ranking'
# print(ranking) # Aqui o resultado será mostrado em forma de lista 'list()' então deverá ser tratado como lista
print(f'{"RANKING DOS JOGADORES":~^30}')
for i, v in enumerate(ranking): # Para tratar o resultado em forma de lista e mostra-lo, use 'indice, valor e enumerate'
    print(f'{i+1}° lugar: {v[0]} tirou {v[1]}') # Aqui v[0] é o nome do jogador e v[1] a quantidade de pontos
    sleep(0.5)
