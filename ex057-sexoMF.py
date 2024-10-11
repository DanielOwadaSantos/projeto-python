'''n=1
while n != 'f' != 'm' != n:
    n=str(input('Digite seu sexo [M/F]: ')).lower()
    if n!= 'f' != 'm' !=n:
        print('\033[31mOpção inválida\nTente novamente\033[m')
    elif n=='m':
        print('\033[36mSeu sexo é MASCULINO.')
    else:
        print('\033[35mSeu sexo é FEMININO\033[m')
print('\033[33mFin')'''


sexo=str(input('Digite seu sexo: [F/M] ')).strip().upper()[0] #Este 0 entre colchetes serve para pegar somente 1° letra
while sexo not in 'MmFf':
    sexo=str(input('Resposta inválida, digite novamente: [F/M] ')).strip().upper()[0]
print('sexo {} registrado com sucesso'.format(sexo))

