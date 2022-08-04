l = float(input('qual a largura da parede? '))
a = float(input('qual a alutra da parede? '))
area = a*l
ql = area/2
print('a largura é {:.2f} q altura é {:.2f}, então a área é {:.2f}m2, vou precisar de {:.2f} litros de tinta'.format(l,a,area,ql))