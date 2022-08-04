vel = float(input('digite uma velocidade '))
print('a velocidade é {}Km/h'.format(vel))
multa = (vel - 80) * 7
if vel > 80:
    print('MULTADO!Voce ultrapassou o limite de velocidade que é R$80km/h e foi multado em R$ {:.2f}'.format(multa))
print('boa viagem')
