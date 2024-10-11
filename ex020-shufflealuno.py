from random import shuffle
a=str(input('Aluno 1= '))
b=str(input('Aluno 2= '))
c=str(input('Aluno 3= '))
d=str(input('Aluno 4= '))
l=[a,b,c,d]
shuffle(l)
print('A ordem de apressntação será {}'.format(l))
