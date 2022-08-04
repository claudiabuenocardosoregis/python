frase = str(input('digite uma frase ')).strip().upper()
print('a letra a aparece {} na frase'.format(frase.count('A')))
print('a primeira letra a aparece na posição {}'.format(frase.find('A')+1))
print('a última letra a aparece na posição {}'.format(frase.rfind('A')+1))

