'''from random import randint
a=randint(1,10)
b=randint(1,10)
c=randint(1,10)
d=randint(1,10)
e=randint(1,10)
tupla=(a,b,c,d,e)
print(f'Os valores foram {tupla}')
print(f'O maior valor foi {max(tupla)}')
print(f'O menor valor foi {min(tupla)}')'''

from random import randint
tupla=(randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print(f'Os valores foram: ')
for n in tupla:
    print(f'{n}',end='')
print(f'\nO maior valor foi {max(tupla)}')
print(f'O menor valor foi {min(tupla)}')





