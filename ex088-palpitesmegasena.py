from random import randint
from time import sleep
titulo = 'PALPITES PARA MEGA SENA'
print(f'{titulo:-^50}')
lista = []
jogos = []
quantidade = int(input('Quantos jogos você quer jogar? '))
total = 1
while total <= quantidade: # esse processo foi feito para designar quantas vezes você deseja jogar
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num) # Faça este processo até aqui, para verificar se o número não será repetido nos palpites
            cont += 1
        if cont >= 6:
            break # Finalize com 'cont e break' para ter a certeza de que os jogos serão feitos com 6 números
    lista.sort() # Use o método sort fora do laço para organizar sua lista
    jogos.append(lista[:])
    lista.clear()
    total += 1
print(f'{f"SORTEANDO {quantidade} JOGOS":-^50}') # Use esta formatação para deixar a lista
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(0.5)
print(f'{"BOA SORTE":~^50}')
