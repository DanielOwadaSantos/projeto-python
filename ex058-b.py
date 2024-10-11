from random import randint
# O randint esta somente antes do while que faz ele randomizar uma vez apenas, diferente do 'ex058-028melhorado'
# que ramdomiza toda vez que acontece o input
comp = randint(1, 10)
print('Tente adivinhar em um número entre 1 e 10: ')
acert = False
p = 0
while not acert:
    jog = int(input('Qual é o número: '))
    p += 1
    if jog == comp:
        acert = True
    else:
        if jog<comp:
            print('Errado, o número é maior, tente outra vez: ')
        elif jog>comp:
            print('Errado, o múmero é menor, tente outra vez: ')
print('Acertou com {} tentativas'.format(p))
