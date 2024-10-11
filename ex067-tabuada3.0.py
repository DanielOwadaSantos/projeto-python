while True:
    n=int(input('Digite um número para ver a tabuada: '))
    if n<0:
        break
    for c in range (1,11):
        print(n,'x',c,'=',(n*c))
print('Acabou')