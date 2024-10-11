'''from math import factorial
n=int(input('Digite um número para calcular o fatorial: '))
f=factorial(n)
print('O fatorial de {} é {}'.format(n,f))'''

n=int(input('Digite um número para calcular o fatorial: '))
c=n
f=1 # fator nulo para multiplicação será sempre 1 enquanto o fator nulo p soma e subtração será 0.
while c>0:
    print('{}'.format(c),end='')
    print(' x 'if c>1 else ' = ',end='')
    f*=c
    c-=1
print(f)
