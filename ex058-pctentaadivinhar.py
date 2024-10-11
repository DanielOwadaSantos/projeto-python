from random import randint
from time import sleep
b=0
c=0
print('_\|/_'*8)
print('Escolha um número entre 0 e 10 e vou adivinhar em algumas tentativas.')
print('_\|/_'*8)
sleep(0.5)
a=int(input('Qual número é? '))#Jogador tenta adivinhar
print('Vamos ver...')
while b!=a:
    b = randint(0, 10)
    c+=1
    if b!=a:
        print('Seu número escolhido foi {}.'.format(b))
        sleep(0.5)
        print('Errei')
        sleep(0.5)
        print('Vou tentar outra vez')
        sleep(0.5)
    elif b==a:
        print('Seu número escolhido foi {}'.format(b))
        print('Achei!')
        sleep(0.5)
print('Mas usei {} tentativas'.format(c))
