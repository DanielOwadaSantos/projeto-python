n=0
listanum=[[],[]]
for c in range(0,6):
    n = int(input(f'Digite o {c}° número: '))
    if n % 2 == 0:
        listanum[0].append(n)
    elif n % 1 == 0:
        listanum[1].append(n)
listanum[0].sort()
listanum[1].sort()
print(listanum[0])
print(listanum[1])

