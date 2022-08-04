v = float(input('qual o valor do produto?'))
vt = v * 5/100
vf = v - vt
print('o valor do produto é R${:.2f}, o desconto será de R${:.2f},o valor final será de R${:.2f}'.format(v, vt, vf))