from random import randint
computador = randint(0, 5)
#print('o computador escolheu {}'.format(computador))
print('-=-' * 20)
jogador = int(input('pensei no número '))
if jogador == computador:
    print('voce venceu')
else:
    print('voce perdeu')
