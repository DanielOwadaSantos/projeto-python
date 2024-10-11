c=s=0
while True: # condição de loop infinito, só para quando ser falso
    n=int(input('Digite um número: '))
    if n==999:
        break # o break está antes da soma para não entrar na soma
    c+=1 # o contador está após o flag para ser desconsiderado o flag(999)
    s+=n
print(f'A soma dos {c} números foi {s}.')
