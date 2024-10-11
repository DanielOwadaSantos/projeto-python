'''co=float(input('Cateto oposto= '))
ca=float(input('Cateto adjacente= '))
hi=(ca**2+co**2)**(1/2)
print('Hipotenusa= {:.2f}'.format(hi))'''

from math import hypot
co=float(input('Cateto opsoto= '))
ca=float(input('Cateto adjacente= '))
hi=hypot(ca,co)
print('Hipotenusa= {:.2f}'.format(hi))
