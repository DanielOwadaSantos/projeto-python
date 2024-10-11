r='S'
c=m=q=ma=me=0
while r in 'Ss':
    n=int(input('Digite um número: '))
    c+=n
    q+=1
    if q ==1:
        ma=me=n
    else:
        if n>ma:
            ma=n
        if n<me:
            me=n
    r=str(input('Quer continuar? [S/N] ')).strip().upper()[0]
m=c/q
print('Você digitou {} números e a média é {}'.format(q,m))
print('O maior valor foi {} e menor foi {}'.format(ma,me))
print('Acabou')
