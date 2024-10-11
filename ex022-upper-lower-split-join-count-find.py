'''a=input('Nome= ')
b=a.upper()
c=a.lower()
d=a.split()
e=''.join(d)
f=len(e)
g=len(d[0])
print(Nome com letras maiúsculas= {}
Nome com letras minúsculas= {}
Número de letras= {}
Número de letras primeiro nome= {}.format(b,c,f,g))'''

n=str(input('Digite seu nome completo: ')).strip()
print('Seu nome com letras maiúsculas é: {}'.format(n.upper()))
print('Seu nome com letras minúsculas é: {}'.format(n.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(n)-n.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(n.find(' ')))
a=n.split()
print('Seu primeiro nome tem {} letras.'.format(len(a[0])))


