a=int(input('Digite um número até 9999= '))
b=a//1%10
c=a//10%10
d=a//100%10
e=a//1000%10
print('''Unidade= {}
Dezena= {}
Centena= {}
Milhar= {}'''.format(b,c,d,e))

'''a=int(input('Digite um número ate 9999: '))
b=str(a)
print('Sua unidade é {}'.format(b[3]))
print('Sua dezena é {}'.format(b[2]))
print('Sua centena é {}'.format(b[1]))
print('Seu milhar é {}'.format(b[0]))'''
