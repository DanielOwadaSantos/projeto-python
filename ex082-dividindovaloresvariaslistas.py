# SOLUÇÃO ENCONTRADA CERTA

listatot=[]
listapar=[]
listaimp=[]
while True:
    n=int(input('Digite um valor: '))
    listatot.append(n)
    if n%2==0:
        listapar.append(n)
    if n%2==1:
        listaimp.append(n)
    r=str(input('Quer continuar [s/n]? '))
    if r in 'Nn':
        break
print(f'A lista total é {listatot}')
print(f'A lista de números pares é {listapar}')
print(f'A lista de números ímpares é {listaimp}')

# SOLUÇÃO CURSO EM VÍDEO

num=list()
pares=list()
impares=list()
while True:
    num.append(int(input('Digite um número: ')))
    r=str(input('Quer continuar [s/n]? '))
    if r in 'Nn':
        break
for i,v in enumerate(num): # criação de laço para analisar cada valor e colocar em suas respectivas listas
    #utilize o par 'i,v'(indice e valor) para fazer a analise junatamente com  'for' 'in' 'enumerate'
    if v%2==0: # se o valor(v) divisivel por 2 ser igual a zero, então o valor é par
        pares.append(v) # use append no 'v' para pegar o valor par após a análise
    elif v%2==1: # se o valor (v) divisivel por 2 for igual a 1 então ele será ímpar
    # nesse caso poderia ser usado o 'else', aqui foi usado 'elif' para estudo e a situação ser mais explícita
        impares.append(v) # use append no 'v' para pegar o valor ímpar após a análise
print(f'A lista completa é {num}')
print(f'A lista de números pares é {pares}')
print(f'A lista de números ímpares é {impares}')
