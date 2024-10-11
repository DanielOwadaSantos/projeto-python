pu=0
pd=0
for b in range (1,6):
    a=float(input('Digite o peso da {}º pessoa: '.format(b)))
    if b==1:
        pu=a
        pd=a
    else:
        if pu<a:
            pu=a
        if pd>a:
            pd=a
print('O maior peso é {}'.format(pu))
print('O menor peso é {}'.format(pd))
