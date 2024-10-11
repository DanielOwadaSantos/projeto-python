from time import sleep
a=float(input('Valor do produto: R$'))
print('\033[1;34mCondiçôes de pagamento\033[m')
sleep(1)
print('1- À vista dinheiro / cheque-\033[33m 10% desconto\033[m')
sleep(1)
print('2- À vista no cartão-\033[33m 5% desconto\033[m')
sleep(1)
print('3- Em até 2X cartão')
sleep(1)
print('4- 3X ou mais-\033[31m 20% de juros\033[m')
sleep(1)
b=int(input('\033[1;34mQual sua forma de pagamento:\033[m'))
if b==1:
    print('O valor de sua compra foi de R${:.2f}'.format(a-(a*10/100)))
elif b==2:
    print('O valor de sua compra foi de R${:.2f}'.format(a-(a*5/100)))
elif b==3:
    print('O valor de sua compra foi de R${:.2f}'.format(a))
elif b==4:
    print('O valor de sua compra foi de R${:.2f}'.format((a*20/100)+a))
else:
    print('\033[31mOpção inválida')
