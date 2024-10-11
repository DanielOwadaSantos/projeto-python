'''a=str(input('Digite um nome: ')).strip()
b='silva'in(a).lower()
print('Contém Silva no nome?')
print(b)'''

nome=str(input('Digite seu nome: ')).strip()
print('Seu nome tem Silva? {}.'.format('silva'in nome.lower()))
