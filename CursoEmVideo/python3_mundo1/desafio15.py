km = float(input('quantos kilometros voce percorreu? '))
d = int(input('quantos dias você ficou com o carro? '))
total = (60 * d) + (km * 0.15)

print('voce pagará R${:.2f}, pelo aluguel do carro'.format(total))
