import math
cata = float(input('qual o valor do cateto a? '))
catb = float(input('qual o valor do cateto b? '))
hi = math.hypot(cata, catb)
print('o valor da hipotenusa é {:.2f}'.format(hi))