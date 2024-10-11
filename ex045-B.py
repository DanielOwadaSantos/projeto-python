from random import randint
from time import sleep
a=('PEDRA', 'PAPEL', 'TESOURA')
b=randint(0,2)
print('''Suas ações
[1]- PEDRA
[2]- PAPEL
[3]- TESOURA''')
c=int(input('Qual sua jogada: '))
print('=-'*11+'=')
print('Computador jogou {}'.format(a[b]))
print('Jogador jogou {}'.format(a[c-1]))
if b==0:
    if c==1:
        print('EMPATE')
    elif c==2:
        print('JOGADOR VENCE')
    elif c==3:
        print('JOGADOR PERDE')
    else:
        print('JOGADA INVÁLIDA')
if b==1:
    if c==1:
        print('JOGADOR PERDE')
    elif c==2:
        print('EMPATE')
    elif c==3:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
if b==2:
    if c==1:
        print('JOGADOR VENCE')
    if c==2:
        print('JOGADOR PERDE')
    if c==3:
        print('EMPATE')
