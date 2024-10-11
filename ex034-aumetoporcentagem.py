'''a=float(input('Qual seu salário? '))
if a>=1250:
    print('Seu aumento foi de 10%')
    print('Você receberá à partir de agora R${:.2f}.'.format((a*10/100)+a))
else:
    print('Seu aumento foi de 15%')
    print('Você receberá à partir de agora R${:.2f}.'.format((a*15/100)+a))'''

a=float(input('Qual seu salário:R$ '))
if a>=1250:
    b=(a*10/100)+a
else:
    b=(a*15/100)+a
print('Quem ganhava R${:.2f}, passa a ganhar R${:.2f}.'.format(a,b))
