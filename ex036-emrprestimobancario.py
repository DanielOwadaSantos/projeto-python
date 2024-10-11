a=float(input('Qual o valor da casa desejada? R$'))
b=float(input('Qual seu salário? R$'))
c=float(input('Quantos anos deseja financiar a casa? '))
d=a/c/12
if d>b*30/100:
    print('\033[;31mSeu empréstimo foi negado por exceder 30% de seu salário!')
    print('\033[;31mSeu financiamento ficaria R${:.2f}.'.format(d))
    print('\033[;31mQue corresponde à {:.2f}% de seu salário.'.format(d/b*100))
else:
    print('\033[;33mParabéns seu empréstimo será financiado!')
    print('\033[;33mSeu fincanciamento ficará R${:.2f}.'.format(d))
    print('\033[;33mQue corresponde à {:.2f}% de seu salário.'.format(d/b*100))
