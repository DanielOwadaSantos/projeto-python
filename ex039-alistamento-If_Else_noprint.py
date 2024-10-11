from datetime import date
a=int(input('Digite seu ano de nascimento:'))
b=date.today().year
if a==b-18:
    print('\033[1;32mEsse ano você deverá se alistar.')
elif b-a>=18:
    d=(b-a)-18
    e=b-d
    print('\033[1;32mVocê passou da hora de se alistar!')
    print('\033[1;32mJá faz {} ano!'.format(d)) if d==1 else print('Já faz {} anos!'.format(d))
    print('Seu ano de alistamento foi {}'.format(e))
elif b-a<=18:
    print('\033[4;33mAinda não é hora de você se alistar.')
    c=18-(b-a)
    f=b+c
    print('\033[4;33mFalta {} ano.'.format(c)) if c==1 else print('Falta {} anos.'.format(c))
    print('Seu ano de alistamento será {}'.format(f))
