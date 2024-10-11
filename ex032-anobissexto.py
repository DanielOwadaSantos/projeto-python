from datetime import date
a=int(input('Digite um ano:'))
if a==0:
    print(date.today().year)
if a%4==0 and a%100!=0 or a%400==0:
    print('Esse ano SIM é bissexto.')
else:
    print('Esse ano NÃO é bissexto')
