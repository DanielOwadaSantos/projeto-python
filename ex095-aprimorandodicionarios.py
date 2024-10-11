time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear() # Limpeza de dados após cada laço
    jogador["nome"] = str(input('Qual nome do jogador? '))
    total_jogos = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear() # Limpeza de dados da lista 'gols' para não acumular
    for c in range(0,total_jogos):
        partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador["gols"] = partidas[:]
    jogador["total"] = sum(partidas)
    time.append(jogador.copy()) # Cópia do 'jogador' que é uma LISTA por isso não pode ser usado fatiamento ([:])
    while True:
        resposta = str(input('Quer continuar [S/N]? ')).upper()[0]
        if resposta in 'SN':
            break
        print('Erro! Responda apenas S ou N por favor.')
    if resposta == 'N':
        break #  ↑ Até aqui foram lido os dados dos jogadores ↑
              #  ↓ Agora vão ser mostrados os dados em uma tabela à partir daqui para baixo ↓
print('cod ', end='')
for i in jogador.keys(): # Cria o cabeçalho da tabela com cada nome dado ao seu dicionário
    print(f'{i:<15} ',end='')
print()
for k, v in enumerate(time): # Cria a tabla com os números
    print(f'{k:>3} ', end=' ')
    for d in v.values():  # Cria os nomes na tabela usando os nomes do dicionário
        print(f'{str(d):<15} ', end=' ')
    print()
# À partir daqui seráo mostrados os dados selecionados pelo usuário ↓
while True:
    busca = int(input('Mostrar dados de qual jogador? Digite 999 para sair.'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Erro! Não existe jogador com esse código {busca}')
    else:
        print(f'- Levantamento do jogador {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'   No jogo {i+1} fez {g} gols.')
print('Encerrando...')
