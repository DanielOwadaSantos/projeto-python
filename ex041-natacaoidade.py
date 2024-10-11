from datetime import date
a=int(input('Qual seu ano de nascimento? '))
b=date.today().year
print('A idade do atleta é {} anos.'.format(b-a))
print('Sua categoria é:')
if b-a<=9:
    print('Mirim')
elif b-a<=14:
    print('Infantil')
elif b-a<=19:
    print('Junior')
elif b-a<=20:
    print('Senior')
else:
    print('Master')