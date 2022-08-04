nome = str(input('Qual é o seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Ana' or nome == 'José' or nome == 'João':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Cláudia':
    print('Seu nome é bem belo')
else:
    print('Seu nome é bem normal!')
print('Tenha um bom dia, {}!'.format(nome))