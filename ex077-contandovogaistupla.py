tupla= 'daniel', 'andreia'
for p in tupla:# o 1º 'for' para analisar cada elemento da tupla
    print(f'\nNa palavra {p.upper()} temos: ',end='') #'p.upper' para destacar a palavra
    for letra in p: # o 2º 'for' para analisar cada letra da palavra pois ela tbm é uma lista
        if letra.lower() in 'aeiou':# para analisar palavras com acentos basta colocar todas as letras com acentos
                                    # 'aàáãâeéèê... etc. letra.lower para jogar a palavra para minúscula
            print(letra,end=' ')
