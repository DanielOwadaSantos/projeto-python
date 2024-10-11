'''a=float(input('Velocidade do carro: '))
if a>80:
    print('Você foi multado!')
    print('O valor de sua multa é R${:.2f}.'.format((a-80)*7))
else:
    print('Pode continuar nessa velocidade!')'''

from time import sleep
print('Limite de velocidade 80 km/h')
sleep(1)
a=float(input('Velocidade do carro: '))
if a>80:
    print('Você foi multado')
    m=(a-80)*7
    print('O valor de sua multa é de R${:.2f}!'.format(m))
print('Tenha um bom dia!')
