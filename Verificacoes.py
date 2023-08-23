valor = input('Digite um valor: ')
print(type(valor))

print('É alfabético? ', valor.isalpha())
print('É numérico? ', valor.isnumeric())
print('É alfanumérico?', valor.isalnum())
print('É formado por letras maiúsculas?', valor.isupper())
print('É formado por letras minúsculas?', valor.islower())
print('É imprimível? ', valor.isprintable())
print('É ASCII?', valor.isascii())
print('É número? ', valor.isdecimal())
print('É identificável? ', valor.isidentifier())
print('Tem só espaços?', valor.isspace())
print('Está em forma de título?', valor.istitle())

#com format

valor1 = input('Digite um valor: ')
print(type(valor))

print('É alfabético? {}'.format(valor1.isalpha()))
print('É numérico? {}'.format(valor1.isnumeric()))
print('É alfanumérico? {}'.format(valor.isalnum()))
print('É formado por letras maiúsculas? {}'.format(valor.isupper()))
print('É formado por letras minúsculas? {}'.format(valor.islower()))
print('É imprimível? {}'.format(valor.isprintable()))
print('É ASCII? {}'.format(valor.isascii()))
print('É número? {}'.format(valor.isdecimal()))
print('É identificável? {}'.format(valor.isidentifier()))
print('Tem só espaços? {}'.format(valor.isspace()))
print('Está em forma de título? {}'.format(valor.istitle()))

