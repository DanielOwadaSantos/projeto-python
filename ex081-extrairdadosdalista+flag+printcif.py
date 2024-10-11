# SOLUÇÃO ENCONTRADA: CERTA

lista=[]
r='S'
quant=0
while r in 'Ss':
    n=int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        lista.sort(reverse=True)
        quant+=1
        r = str(input('Quer continuar?[s/n]'))
    if r in 'Nn':
        break
print(f'Sua lista tem {quant} elementos.')
print('O número 5 faz parte da lista' if 5 in lista else 'O 5 não faz parte.')
print(f'A lista na ordem decrescente é {lista}')

# SOLUÇÃO CURSO EM VÍDEO

valores=[]
while True:
    valores.append(int(input('Digite um valor: ')))
    r=str(input('Quer continuar [s/n]? '))
    if r in 'Nn':
        break
print(f'Sua lista tem {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'A lista em ordem decrescente é {valores}')
if 5 not in valores:
    print('O número 5 não faz parte da lista.')
else:
    print('O número 5 faz parte da lista.')