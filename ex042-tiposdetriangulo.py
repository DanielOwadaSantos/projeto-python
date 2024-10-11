a=float(input('Primeiro segmento: '))
b=float(input('Segundo segmento '))
c=float(input('Terceiro segmento: '))
if a+b>c and a+c>b and b+c>a:
    print('Sim, se pode formar um triângulo.')
    if a==b==c:
        print('Seu triãngulo é equilátero.')
    elif a!=b!=c!=a:
        print('Seu triângulo é escaleno.')
    else:
        print('Seu triângulo é isósceles.')
else:
    print('Não se pode formar um triângulo.')

