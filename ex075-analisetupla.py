tupla=int(input('Digite um número: ')),int(input('Digite outro número: ')),\
int(input('Digite outro número: ')),int(input('Digite outro número: '))
print(f'Você digitou os valores {tupla}.')
print(f'O número 9 apareceu {tupla.count(9)} vezes.')# use COUNT para contar um item(valor) dentro de uma tupla no caso '9'.
if 3 in tupla:# use esse método(IF/ELSE e IN) para verificar se um valor está correspondendo à tupla.
    print(f'O número 3 apareceu na {tupla.index(3)+1}º posição.')#use INDEX para mostrar em que posição aparece tal valor(3)
else:
    print('O valor 3 não existe.')
print('Os números pares são:')
for n in tupla:
    if n %2==0:
        print(n,end=' ')