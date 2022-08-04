a = int(input('Primeiro número '))
b = int(input('Segundo número '))
c = int(input('Terceiro número '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor número digitado foi {} e o maior número digitado foi {}'.format(menor, maior))
