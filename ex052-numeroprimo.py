'''a=int(input('Digite um número: '))
c=0
for b in range (1,a+1):
    if a % b == 0:
        c+=1
if c==2:
    print('Esse número é primo')
else:
    print('Esse número não é primo')'''

a=int(input('Digite um número: '))
c=0
for b in range (1,a+1):
    if a%b==0:
        c+=1
        print('\033[33m',end='')
    else:
        print('\033[31m',end='')
    print(b,end='')
if c ==2:
    print('\033[m\nEsse número é primo')
else:
    print('\033[m\nEsse número não é primo, ele foi divisíel {} vezes.'.format(c))
