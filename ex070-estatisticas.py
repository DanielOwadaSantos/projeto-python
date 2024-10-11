t = mm = b = c = 0
nb = ''
while True:
    n = str(input('Nome do produto: '))
    p = float(input('Preço do produto: '))
    c+=1
    t += p
    if p > 1000:
        mm += 1
    if c == 1 or p < b:
        b = p
        nb = n
    r = ' '
    while r not in 'sn':
        r = str(input('Quer continuar?[s/n] ')).strip().lower()[0]
    if r == 'n':
        break
print(f'O total da compra foi {t:.2f}, {mm} produto custa mais de 1000 reais e {nb} foi o mais barato.')
print('{:-^40}'.format('FIM DO PROGRAMA'))
