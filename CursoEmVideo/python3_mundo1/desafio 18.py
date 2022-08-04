import math
angulo = float(input('Qual o valor do ângulo? '))
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print('o valor do ângulo de {} tem o seno de {:.2f} e o cosseno de {:.2f} e a tangente de {:.2f} '.format(angulo, sen, cos, tan))


