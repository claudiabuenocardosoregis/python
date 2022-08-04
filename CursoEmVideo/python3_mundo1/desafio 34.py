sal = float(input('Qual o salário do funcionário? R$ '))
if sal > 1250:
    print('quem ganhava R${:.2f}, passa a ganhar R${:.2f}'.format(sal, sal * 10 / 100 + sal))
else:
    print('quem ganhava R${:.2f}, passa a ganhar R${:.2f}'.format(sal, sal * 15 /100 + sal))


