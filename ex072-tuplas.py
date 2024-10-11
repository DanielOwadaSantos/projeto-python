ne='zero','um','dois','três','quatro','cinco','seis',\
    'sete','oito','nove','dez','onze','doze','treze',\
    'quatorze','quinze','dezesseis','dezessete',\
    'dezoito','dezenove','vinte'
resp=' '
while True:
    c = int(input('Digite um número entre 0 e 20: '))
    if 0 <= c <= 20 :
        print(f'Você digitou o número {ne[c]}')
        resp = str(input('Quer continuar?[s/n] ')).strip().lower()[0]
        if resp =='n':
            break
print('Acabou')


