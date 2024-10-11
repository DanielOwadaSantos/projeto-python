from math import trunc
med=0
hv=0
hn=''
m20=0
for d in range (1,5):
    a=str(input('Digite seu nome: ')).strip()
    b=int(input('Digite sua idade: '))
    c=str(input('Sexo M/F: ')).strip()
    if b>0:
        med+=b
    if c in'Mm' and c==1:
        hv=b
        hn=a
    if c in 'Mm' and b>hv:
        hv=b
        hn=a
    if c in 'Ff' and b<20:
        m20+=1
print('A média de idade do grupo é de {}'.format(trunc(med/4)))
print('o homem mais velho tem {} anos e se chama {}'.format(hv,hn))
print('{} mulheres tem menos de 20 anos'.format(m20))

