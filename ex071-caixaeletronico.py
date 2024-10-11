v=int(input('Qual valor deseja sacar? '))
tot=v
ced=50
tced=0
while True:
    if tot>=ced:
        tot-=ced
        tced+=1
    else:
        if tced>0:
            print(f'Total de {tced} cédulas de R${ced} ')
        if ced==50:
            ced=20
        elif ced ==20:
            ced =10
        elif ced ==10:
            ced=1
        tced=0
        if tot==0:
            break
print('Fim')
