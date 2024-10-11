a=float(input('Nota 1= '))
b=float(input('Nota 2= '))
c=(a+b)/2
if c<5:
    print('\033[;31mReprovado!!!')
    print('\033[;31mSua média foi {:.1f}'.format(c))
elif c>5 and c<7:
    print('Recuperação!!!')
    print('Sua média foi {:.1f}'.format(c))
else:
    print('\033[1;33mAprovado!!!')
    print('\033[1;33mSua média foi {:.1f}'.format(c))
