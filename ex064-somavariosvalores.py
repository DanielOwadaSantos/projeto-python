a=c=s=0
a = int(input('Digite um número [999 PARAR]: '))
while a != 999:
    s += a
    c+=1
    a=int(input('Digite um número [999 PARAR]: ')) # o flag está na última linha para poder funcionar
print('A soma dos valores foi {} e você digitou {} números.'.format(s,c))
print('Fim')
