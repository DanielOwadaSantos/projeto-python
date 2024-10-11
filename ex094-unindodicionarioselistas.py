galera = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa["nome"] = str(input('Nome: '))
    while True:
        pessoa["sexo"] = str(input('Sexo[M/F]: ')).upper()[0]
        if pessoa["sexo"] in 'MF':
            break
        print('Erro. Digite apenas M ou F por favor.')
    pessoa["idade"] = int(input('Digite sua idade: '))
    soma += pessoa["idade"]
    galera.append(pessoa.copy())
    while True:
        resposta = str(input('Quer continuar [S/N]? ')).upper()[0]
        if resposta in 'SN':
            break
        print('Erro. Digite apenas S ou N por favor.')
    if resposta == 'N':
        break
print(galera)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma/ len(galera)
print(f'A média de idade é de {media:5.2f} anos.')
print('A lista de mulheres cadastradas é: ', end='')
for p in galera:
    if p["sexo"] in 'Ff':
        print(f'{p["nome"]}', end=' ')
print()
print('Lista das pessoas acima da média:')
for p in galera:
    if p["idade"] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v} ', end='')
        print()
print('Programa encerrado!')
