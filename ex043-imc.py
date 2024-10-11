a=float(input('Qual seu peso: '))
b=float(input('Qual sua altura: '))
c=a/b**2
print('I.M.C: {:.2f}'.format(c))
if c<18.5:
    print('Abaixo do peso')
elif 18.5<=c<25:
    print('peso ideal')
elif 25<=c<30:
    print('Sobrepeso')
elif 30<=c<40:
    print('Obesidade')
else:
    print('Obesidade morbida')