def ficha(nome="'Sem nome'", gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


nome_jogador = str(input('Nome do jogador: '))
quant_gols = str(input('Quantos gols marcados: '))
if quant_gols.isnumeric():
    quant_gols = int(quant_gols)
else:
    quant_gols = 0
if nome_jogador.strip() == '':
    ficha(gols=quant_gols)
else:
    ficha(nome_jogador, quant_gols)
