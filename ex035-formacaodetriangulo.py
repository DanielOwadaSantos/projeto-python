'''a=float(input('Primeiro segmento: '))
b=float(input('Segundo segmento: '))
c=float(input('Terceiro segmento: '))
if (b-c)<a<b+c and (c-a)<b<c+a or(b-a)<c<b+a:
    print('Sim, se pode formar um triângulo.')
else:
    print('Não se pode formar um triângulo.')'''

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a + b > c and b + c > a and a + c > b:
    print('Sim, se pode formar um triângulo.')
else:
    print('Não se pode formar um triângulo.')
