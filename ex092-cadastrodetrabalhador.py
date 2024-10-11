from datetime import datetime
dados = {}
dados['nome']= str(input('Nome: '))
anonascimento = int(input('Ano de nascimeto: '))
dados['idade'] = datetime.now().year - anonascimento
dados['ctps'] = str(input('Carteira de trabalho (digite 0 não tem): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salãrio: '))
    dados['aposentadria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
for k, v in dados.items():
    print(f'{k} tem o valor {v}')