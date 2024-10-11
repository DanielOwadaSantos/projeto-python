def area(a, b):
    area_total = a * b
    print(f'A área total do terreno de {a}x{b}m é de {area_total}m².') # para digitar metros quadrados aperte alt+0178

print('CONTROLE DE TERRENOS')
print('-'*20)
a = float(input('Largura do terreno (m): '))
b = float(input('Comprimento do terreno (m): '))

area(a, b)

