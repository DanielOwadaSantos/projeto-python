from random import randint
from time import sleep
print('*** JOGO PAR OU ÍMPAR ***')
c=1
while True:
    comp = randint(0, 10)
    n=int(input('Diga um número: '))
    pi=str(input('Escolha PAR ou ÍMPAR [P/I] >>> ')).strip().upper()[0]
    s = n + comp
    if pi != 'P' and pi != 'I':
        print('Opção inválida tente novamente.')
    else:
        print(f'''Jogador jogou:{n} 
Computador jogou: {comp}''')
        sleep(0.5)
        if s%2==0:
            print(s,'Deu PAR!')
            if s%2==0 and pi == 'P':
                print('Venceu!')
            elif s%2==0 and pi=='I':
                print('Perdeu')
                break
        if s%2==1:
            print('Deu ÍMPAR!')
            if s % 2 == 1 and pi == 'I':
                print('Venceu')
            elif s%2==1 and pi == 'P':
                print('Perdeu!')
                break
    sleep(0.5)
    c+=1
print(f'Jogador jogou {c} vezes.')
print('Fim')