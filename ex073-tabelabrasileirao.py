brasileiro2023='Botafogo','Bragantino','Grêmio','Palmeiras','Flamengo','Fortaleza','Fluminense','Athletico-PR',\
'Atlético-MG','São Paulo','Cuiabá','Internacional','Cruzeiro','Corinthians','Santos','Bahia','Vasco da Gama',\
'Goiás','Coritiba','América-MG'
print('A classificação do Brasileirão 2023 é: ')
c=1
for t in brasileiro2023:
    print(f'{c}°- {t}')
    c += 1
print('A ordem alfabética dos times é: ')
print(sorted(brasileiro2023))
print('Os 5 primeiros são:')
print(brasileiro2023[:5])
print('os 4 últimos são: ')
print(brasileiro2023[16:])#pode ser [-4:] tbm
#cori=(brasileiro2023.index('Corinthians')+1)
print(f'O Corinthians está na {brasileiro2023.index("Corinthians")+1}° posição.')


