def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError,TypeError):
            print(f'\033[31mErro!!! Por favor digite um número inteiro...\033[m')
            continue
        except(KeyboardInterrupt):
            print(f'\033[31mPrograma interrompido...\033[m')
            return 0
        else:
            return n





n = leiaint('Digite um número inteiro: ')
print(f'O valor digitado foi {n}.')