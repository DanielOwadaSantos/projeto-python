'''a=input('Digite uma frase: ')
c=a.count('a')
d=a.find('a')
e=a.split(a)
print('A letra "a" aparece {} vezes.
Aparece na posição {} pela primeira vez.
Aparece na última vez na posição {}.'.format(c,d,e))'''

a=str(input('Digite uma frase: ')).lower().strip()
print('A letra "A" aparece {} vezes na frase.'.format(a.count('a')))
print('A letra "A" aparece pela primeira vez na posição {}.'.format(a.find('a')+1))
print('A letra "A" aparece pela última vez na posição {}.'.format(a.rfind('a')+1))
