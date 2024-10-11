from time import sleep

def maior(*num): # Colocando '*' na frente do parâmetro significa que serãp definidos vários parâmetros e que
                # serão desempacotados utilizando uma estrutura de repetição
    contador = maior_numero = 0
    print('-'* 40)
    for valor in num:
        print(f'{valor}',end=' ')
        sleep(0.3)
        if contador == 0:
            maior_numero = valor
        else:
            if valor > maior_numero:
                maior_numero = valor
        contador += 1
    print(f'Foram analisados {contador} números')
    print(f'O maior número deles é {maior_numero}')

maior(1, 2, 3, 4)
maior(7, 2, 0)
maior(21, 45, 60, 2)
maior()
