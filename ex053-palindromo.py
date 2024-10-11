'''a=str(input('Digite uma frase: ')).strip().upper()
b=a.split()
d=''.join(b)
e=d[::-1]
if d==e:
    print('{}, {}- Esta palavra é um palindromo'.format(d,e))
else:
    print('{}, {}- Esta palavra não é um palindromo'.format(d,e))'''

a=str(input('Digite uma frase: ')).strip().upper()
b=a.split()
c=''.join(b)
e=''
for d in range(len(c)-1,-1,-1):
    e+=c[d]
if e==c:
    print('{} = {}- Essa palavra/ frase é um palíndromo.'.format(e,c))
else:
    print('Não é um palíndromo')