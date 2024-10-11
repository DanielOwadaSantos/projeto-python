matriz = [0,0,0],[0,0,0],[0,0,0]
numpar = 0
for c in range (0,3):
    for l in range (0,3):
        matriz[c][l] = int(input(f'Digite um valor para {[c],[l]}:'))
for c in range (0,3):
    for l in range (0,3):
        print(f'[{matriz[c][l]}]',end='')
        if matriz[c][l] % 2 == 0:
            numpar += matriz[c][l]
    print()
print(f'A soma dos valores pares é {numpar}')