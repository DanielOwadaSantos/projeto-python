p18=h=m20=0
while True:
    id=int(input('Digite sua idade: '))
    sx = ' '
    while sx not in 'fm':
        sx= str(input('Digite seu sexo [f/m]: ')).strip().lower()[0]
    if id >= 18:
        p18 += 1
    if sx == 'm':
        h+=1
    if sx == 'f' and id <=20:
        m20+=1
    r = ' '
    while r not in 'sn':
        r=str(input('Quer continuar [s/n]? ')).strip().lower()[0]
    if r == 'n':
        break
print(f'Foram cadastrados {p18} pessoas maiores de 18 anos, {h} homens e {m20} mulheres com menos de 20 anos ')
print('Acabou')






