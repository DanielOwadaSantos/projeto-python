numaior=numenor=posima=posime=0
valores=list()
for c in range (1,6):
    valores.append(int(input('Digite um valor:')))
for c,v in enumerate(valores):
    if c==0:
        numenor=numaior=v
    else:
        if v>numaior:
            numaior=v
            posima=c
        if v<numenor:
            numenor=v
            posime=c
print(f'Os valores foram {valores}')
print(f'O número maior foi {numaior} e está na posição \033[1;4;31m{posima+1}\033[m'
      f' e o número menor foi {numenor} e está na posição \033[1;4;31m{posime+1}\033[m.')

# RESOLUÇÃO CURSO EM VÍDEO - PERMITE ANALISAR MAIS DE UMA POSIÇÃO (MAIOR OU MENOR)

listanum = []
mai=0
men=0
for c in range(0,5):
    listanum.append(int(input(f'Digite um valor para posição {c}: ')))
    if c == 0:# se 'c' for o 1° valor lido(no caso 0) então ele será o maior e tbm o menor
        mai=men=listanum[c]
    else:
        if listanum[c] > mai:
            mai=listanum[c]
        if listanum[c] < men:
            men=listanum[c]
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {mai} nas posições ',end='')
for i,v in enumerate(listanum):# 'indice' e 'valor' para o enumerate
    if v == mai:# aqui 'v' seria o mesmo que listanum[i]
        print(f'{i}-',end='')# aqui será printado o número do índice '{i}'
print()# print para quebra de linha
print(f'O menor valor digitado foi {men} nas posições ',end='')
for i,v in enumerate(listanum):
    if v == men:
        print(f'{i}-',end='')
print()