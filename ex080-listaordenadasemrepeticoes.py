# SOLUÇÃO ERRADA

'''valores=[]
for c in range(1,6):
    n=int(input(f'Digite o {c}° valor: '))
    valores.insert(n,c)
for c,v in enumerate(valores):
    if v==c:
        valores.insert(c,v)
print(valores)'''

# SOLUÇÃO CURSO EM VÍDEO

lista=[]
for c in range(0,5):
    n=int(input('Digite um valor: '))
    #if c == 0: # se 'c' for igual a zero,'n' será add no 1° valor
    #    lista.append(n)
    #elif n > lista[-1]: # use 'lista[len(lista)-1]' ou ' lista[-1]' para pegar o último valor. Se 'n' for maior que o
                                  # último valor então será feito o append
    #   lista.append(n) # como existem duas funções praticamente iguais ou o mesmo comando, podemos usar assim:,
    if c == 0 or n > lista[-1]: # Assim o comando fará append se for o 1°(lista==0), ou maior que o último valor
                                    # (n > lista[-1])
        lista.append(n)
        print('Adicionado no final da lista...')
    else:# Para descobrir em que posição add, faça o vetor andar de posição para isso faça assim:
        pos=0
        while pos < len(lista): # para ir da posição 0(pos=0) até o fim da lista(len(lista)
            if n <= lista[pos]: # para verificar se o numero inserido 'n' é menor ou igual ao ja contido ou a ele dentro
                                # de cada posição'lista[pos]',e se ele for menor será add numa posição específica assim:
                lista.insert(pos,n) # use lista.insert(pos,n) para inserir na posição(pos) o valor(n)
                print(f'Adicionado na posição {pos} da lista...')
                break # Após a  inserção use o break pois será inserdo somente uma vez na lista
            pos += 1 # use esse comando detro do 'if' para ir passado para a próxima posição e colocando em ordem
print(f'Os valores digitados em ordem são {lista}')
