c=0
d=0
for a in range(0,6):
    b=int(input('Digite um número: '))
    if b%2==0:
        d+=1
        c+=b
print('A soma dos {} números pares é {}'.format(d,c))