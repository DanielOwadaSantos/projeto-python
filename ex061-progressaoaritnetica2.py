n1=int(input('Digite o primeiro termo: '))
r=int(input('Digite a razão: '))
q=int(input('Digite quantos termos deseja ver: '))
t=n1
c=1
while c <= q:
    print(t,'-',end=' ')
    t+=r
    c+=1
print('FIM')

