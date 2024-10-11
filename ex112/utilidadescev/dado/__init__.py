def leiadinheiro(msg):
    valido = False
    while True:
        entrada = str(input(msg)).strip().replace(',','.')
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO \"{entrada}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)
