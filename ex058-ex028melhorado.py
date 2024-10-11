from random import randint
from time import sleep
b=randint(0,1) #Faz o computador pensar
d=0
print('_\|/_'*8)
print('Tente adivihar um número entre 0 e 10.')
print('_\|/_'*8)
sleep(0.5)
a=int(input('Qual número é? >>> '))#Jogador tenta adivinhar
print('Vamos ver...')
sleep(0.5)
while b!=a:
    b=randint(0,1)
    d+=1
    print('Meu número escolhido foi: >>> {}'.format(b))
    sleep(0.5)
    if b!=a:
        c=int(input('Você ERROU!!! Tente outra vez: >>>  '))
    if b==a:
        print('Acertou!!!')
print('Mas você usou {} tentativas'.format(d))
if d==1:
    print('Parabéns')

