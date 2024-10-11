# SOLUÇÃO COMPLETADA COM AJUDA DA AULA

galera=list()
dado=list()
pesomaior=list()
pesomenor=list()
t=mai=men=0
while True:
    dado.append(str(input('Qual seu nome? ')))
    dado.append(float(input('Qual seu peso? ')))
    if len(galera)==0:
        mai=men=dado[1]
    else:
        if dado[1] > mai:
            mai = dado[1]
        if dado[1] < men:
            men = dado[1]
    galera.append(dado[:])
    dado.clear()
    r=' '
    while r not in 'sn':
        r=str(input('Quer continuar [s/n]? ')).strip().lower()[0]
        t+=1
    if r == 'n':
        break
for p1 in galera:
    if p1[1]==mai:
        pesomaior.append(p1)
for p1 in galera:
    if p1[1]==men:
        pesomenor.append(p1)
print(f'O total de pessoas cadastradas foi de {t}')
print(f'A lista de pessaos pesadas é {pesomaior} e a lista de pessoas leves é {pesomenor}.')

# SOLUÇAO CURSO EM VÍDEO

temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Qual seu nome? ')))
    temp.append(float(input('Qual seu peso? ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai :
            mai = temp[1]
        if temp[1] < men :
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    r = str(input('Quer continuar?'))
    if r in 'Nn':
        break
print(f'Ao todo você cadastrou {len(princ)} pessoas.')
print(f'O peso maior foi de {mai}Kg. Peso de: ',end='')
for p in princ:
    if p[1] == mai :
        print(f'[{p[0]}]',end='')
print()
print(f'O peso menor foi de {men}Kg. Peso de: ',end='')
for p in princ:
    if p[1] == men :
        print(f'[{p[0]}]',end='')
print()
