'''a=float(input('Distância da viagem em km: '))
if a<=200:
    print('O valor de sua passagem é de R${:.2f}.'.format(a*0.50))
else :
    print('O valor de sua passagem é de R${:.2f}.'.format(a*0.45))'''

a=float(input('Distância da viagem em km: '))
b=a*0.50 if a<=200 else a*0.45
print('O valor de sua viagem é de R${:.2f}'.format(b))
