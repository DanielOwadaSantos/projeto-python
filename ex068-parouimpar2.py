from random import randint
v=0
while True:
    j=int(input('Digite um número: '))
    c=randint(0,10)
    to=j+c
    ti=' '
    while ti not in 'PI':
        ti=str(input('Par ou Ímpar? [P/I] :')).strip().upper()[0]
    print(f'Você jogou {j} e o computador jogou {c}.')
    print(f'Deu PAR' if to%2==0 else 'Deu Ímpar')
    if ti=='P':
        if to%2==0:
            print('Você VENCEU!!!')
            v+=1
        else:
            print('Você PERDEU!!!')
            break
    elif ti=='I':
        if to%2==1:
            print('Você VENCEU!!!')
            v+=1
        else:
            print('Você PERDEU!!!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER. VOCÊ GANHOU {v} VEZES!!!')
