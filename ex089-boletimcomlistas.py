ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome,[nota1, nota2],media]) # Use desta maneira para declarar uma lista dentro da outra '([])'
    resposta = str(input('Quer continuar? '))
    if resposta in 'Nn':
        print('FINALIZANDO...')
        break
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}') # Aqui foi criado uma 'tabela' ou indice para mostrar os resultados
print('-'*30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}') # Aqui será mostrado a tabela.Faça as formatações exatamente como na tabela
while True:
    opc = int(input('Mostrar nota de qual aluno? (999 para finalizar)')) # Aqui será mostrado o índice do aluno desejado
                                                                    # de acordo com os valores mostrados anteriormente
    if opc == 999:
        break
    if opc <= len(ficha)-1: # Se o número digitado for menor do que o de alunos cadastrados poderá ser mostrado as notas
        print(f'As notas de {ficha[opc][0]} são {ficha[opc][1]}') # Aqui 'opc' é o número do aluno ou índice
