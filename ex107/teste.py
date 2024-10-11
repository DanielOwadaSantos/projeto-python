from ex107 import moeda

p = float(input('Digite o valor desejado: '))
print(f'O dobro de {p} reais é {moeda.dobro(p)} reais.')
print(f'A metade de {p} reais é {moeda.metade(p)} reais.')
print(f'Aumentando 10% de {p} temos {moeda.aumentar(p, 10)} reais.')
print(f'Diminuindo 13% de {p} temos {moeda.diminuir(p, 13)} reais.')
