jogador = {}
partidas = []
jogador['nome'] = str(input('Qual o nome do jogador? '))
total_jogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
# Agora você vai precisar saber quantos gols foram feitos em cada partida para isso use o 'for' e crie uma lista
for c in range(0,total_jogos):
    partidas.append(int(input(f'Quantos gol na partida {c}: ')))
# Aqui você deve colocar a lista dentro do dicionário, para isso faça assim:
jogador['gols'] = partidas[:] # Aqui foi colocado a lista de 'partidas' dentro do dicionário 'gols'
jogador['total'] = sum(partidas) # Este comando serve para somar todos os 'gols' que foram colocados nas listas
                                # 'partidas' e depois tbm foram colocados dentro de um dicionário
print('-'*30)
print(jogador)
print('-'*30)
for k,  v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-'*30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} jogos.')
for i, v in enumerate(jogador["gols"]):
    print(f'   → Na partida {i}, fez {v} gols')
print(f'O jogador {jogador["nome"]} tem um total de {jogador["total"]} gols.')
