# solução incompleta
valores=[]
while True:
    valores.append(int(input('Digite um valor: ')))
    r = ' ' # nessa posição, ápos while, a variável 'r' permite que a próxima função('while r not in 'sn')entre em loop
            # do contrário se estivesse antes do 1° while a função seguinte não entraria em loop
    while r not in 'sn':
        r=str(input('Quer continuar [s/n]? '))
    if r=='n':
        break
print(sorted(valores))

# solução curso em video

valores=[]
while True:
    n=int(input('Digite um número: '))
    if n not in valores:
        valores.append(n)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado. Tente novamente.')
    r=str(input('Quer continuar?[s/n] '))
    if r in 'nN':
        break
valores.sort()
print(f'Os valores digitados em ordem são {valores}')