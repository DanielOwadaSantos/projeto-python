from datetime import date
b = date.today().year
e=0
f=0
for d in range (1,8):
    a=int(input('Digite sua data de nascimento:'))
    c=b-a
    if c>=21:
        e+=1
    else:
        f+=1
print('{} pessoas são de maior.'.format(e))
print('{} pessoas são de menor.'.format(f))
