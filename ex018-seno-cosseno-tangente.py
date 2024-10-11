'''import math
n = float(input('Ângulo= '))
a = math.radians(n)
b = math.sin(a)
c = math.cos(a)
d = math.tan(a)
print('Seno= {:.2f}\nCosseno={:.2f} \nTangente={:.2f}'.format(b, c, d))'''

from math import radians, sin, cos, tan
n=float(input('Ângulo= '))
a=radians(n)
b=sin(a)
c=cos(a)
d=tan(a)
print('Seno= {:.2f}\nCosseno= {:.2f}\nTangente= {:.2f}'.format(b,c,d))
