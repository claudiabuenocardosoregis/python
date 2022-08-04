sal = float(input('qual é o salário do funcionário? '))
va = sal * 15/100
sf = va + sal
print('seu salário é de R${:.2f}, teve R${:.2f} de aumento, seu salário final será de R#{:.2f}'.format(sal, va, sf))