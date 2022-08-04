nome = str(input('qual é o seu nome? ')).strip()
print('seu nome em maiúsculo é {}'.format(nome.upper()))
print('seu nome em minúsculo é {}'.format(nome.lower()))
print('seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
#print('o primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))




