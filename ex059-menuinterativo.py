n1=int(input('Digite um número: '))
n2=int(input('Digite outro número: '))
opção=0
while opção!=5:
   # Ao usar aspas triplas
    print('''ESCOLHA UMA OPÇÃO A SEGUIR:
    [1]SOMAR
    [2]MULTIPLICAR
    [3]MAIOR DOS DOIS
    [4]NOVOS NÚMEROS
    [5]FINALIZAR PROGRAMA''')
    opção=int(input('Qual sua opção: '))
    if opção == 1:
        print(n1+n2)
    elif opção == 2:
        print(n1*n2)
    elif opção == 3:
        if n1>n2:
            print('{} é o maior'.format(n1))
        elif n2>n1:
            print('{} é o maior'.format(n2))
        else:
            print('Os dois números são iguais.')
    elif opção == 4:
        n1=int(input('Digite um número: '))
        n2=int(input('Digite outro número: '))
    elif opção == 5 :
        print('FINALINZANDO...')
    else:
        print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE.')
print('FIM DO PROGRAMA.')
