a=int(input('Digite um número: '))
print('''Opção para base de conversão
[1]-BINÁRIO
[2]-OCTAL
[3]-HEXADECIMAL''')
b=int(input('Digite uma opção:'))
if b==1:
    print('{} convertido para binário é \033[34m{}\033[m'.format(a,bin(a)[2:]))
elif b==2:
    print('{} convertido em octal é \033[34m{}\033[m'.format(a, oct(a)[2:]))
elif b==3:
    print('{} convertido em hexadecimal é \033[34m{}\033[m'.format(a, hex(a)[2:]))
else:
    print('\033[;31mOpção invalida!\033[m')
