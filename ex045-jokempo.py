from random import choice
from time import sleep
print('\033[1;32m*4i20'*4+'*\033[m')
print('\033[1;4;33mVAMOS JOGAR JOKEMPÔ\033[m')
r='pedra'
p='papel'
t='tesoura'
a=[p,r,t]
b=choice(a)
print('\033[1;4;33mESCOLHA ENTRE :\033[m')
print('\033[1;32m*4i20'*4+'*\033[m')
sleep(1)
print('\033[1;37m1- PEDRA')
sleep(1)
print('2- PAPEL')
sleep(1)
print('3- TESOURA\033[m')
c=input('Digite sua opção: ')
sleep(1)
print('\033[1;;35;40mJO\033[m')
sleep(1)
print('\033[7;31;40mKEM\033[m')
sleep(1)
print('\033[1;7;3007;40mPO\033[m')
sleep(1)
if c=='1':
    print('\033[1;37mVocê escolheu PEDRA')
elif c=='2':
    print('Você escolheu PAPEL')
elif c=='3':
    print('Você escolheu TESOURA\033[m')
else:
    print('\033[31mOpção inválida\033[m')
print('Eu {}.'.format(b.upper()))
if c=='1' and b==r or c=='2' and b==p or c=='3' and b==t:
    print('\033[1;4;35mO JOGO EMPATOU!\033[m')
elif c=='1' and b==t or c=='2' and b==r or c=='3' and b==p:
    print('\033[1;4;36mPARABÉNS VOCÊ VENCEU!!!!!!!!!\033[m')
else:
    print('\033[1;4;31mVOCÊ PERDEU!!!!!!!!!!\033[m')

