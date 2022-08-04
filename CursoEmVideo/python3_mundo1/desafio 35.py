a = float(input('qual o valor da reta 1: '))
b = float(input('qual o valor da reta 2: '))
c = float(input('qual o valor da reta 3: '))
if (a < b + c) and (b < a + c) and (c < a + b):
    print('Os segmentos acima FORMAM um triângulo')
else:
    print('Os segmentos acima NÃO FORMAM um triângulo')


