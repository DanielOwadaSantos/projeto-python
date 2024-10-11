'''import random
import emoji
a=[1,2,3,4,5]
b=random.choice(a)
c=int(input('Escolha um número entre 1 e 5: '))
print('Meu número escolhido foi {}.'.format(b))
if c == b:
    print('Parabéns você acertou!', end='')
    print(emoji.emojize(':face_with_monocle:')*20)
else:
    print('Tente outra vez!')'''

from random import randint
from time import sleep
b=randint(0,5) #Faz o computador pensar
print('_\|/_'*8)
print('Tente adivihar um número entre 0 e 5.')
print('_\|/_'*8)
a=int(input('Qual número é? '))#Jogador tenta adivinhar
print('Vamos ver...')
sleep(3)
if b==a:
    print('Meu número escolhido foi {}.'.format(b))
    print('Parabéns vc acertou!')
else:
    print('Meu número escolhido foi {}\nVocê errou!\nTente outra vez!'.format(b))
