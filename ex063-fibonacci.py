qt=int(input('Quantos termos: '))
t1=0
t2=1
print(t1,'-',t2,end=' ')
c=3 # Nesse caso o contador começou com 3 pois 2 termos já foram mostrados antes (t1 e t2)
while c<=qt:
    t3=t1+t2
    print('-',t3,end=' ')
    t1=t2
    t2=t3
    c+=1
print('- Fim')