dis = float(input('qual a distancia da viagem? '))
print('a distancia é de {} Km'.format(dis))
if dis <= 200:
    preço = dis * 0.50
else:
    preço = dis * 0.45
print('você pagara R$ {:.2f}'.format(preço))
