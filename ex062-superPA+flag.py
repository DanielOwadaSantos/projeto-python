n1=int(input('Digite o primeiro termo: '))
r=int(input('Digite a razão: '))
q=int(input('Digite quantos termos deseja ver: '))
t=n1
c=1
tot=0
mt=q
while mt!=0:
    tot+=mt
    while c <= tot:
        print(t,'-',end=' ')
        t+=r
        c+=1
    print('Pausa')
    mt=int(input('Deseja ver mais quantos termos: '))
print('Sua PA usou {} termos'.format(tot))
print('FIM')