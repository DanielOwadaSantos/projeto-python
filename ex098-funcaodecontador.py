from time import sleep

def contador(i, f, p): # função def com necessidade de parâmetros que devem ser definidos (início, fim, passo)
    if p < 0:
        p *= -1#
    if p == 0:
        p = 1
    print('=' * 40)
    print(f'Contagem de {i} até {f} pulando de {p} em {p}...')
    sleep(2) # Este sleep serve para dar tempo do usuáro ler o cabeçalho

    if i < f: # Este if é necessário pois é possível dar início(i) com valor menor e maior que o fim(f), sem esta função
              # não seria possível completar esta ação com o else em seguida
        cont = i # variável cont com valor 'i' de início, que primeiramente foi definida como '1'
        while cont <= f: # Aqui o parâmetro definido como 'f' ou 'final' primeiramente foi '10'
            print(f'{cont}',end=' ')
            sleep(0.5)
            cont += p # Aqui o parâmetro definido como 'p' ou 'passo' primeiramente foi '1'
        print('Fim')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}',end=' ')
            sleep(0.5)
            cont -= p
        print('Fim')
    sleep(1)


# Programa principal com os parâmetros definidos
contador(0, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de escolher...')
inicio = int(input('Início: '))
final = int(input('Final: '))
passo = int(input('Passo: '))
contador(inicio, final, passo)
