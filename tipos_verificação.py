#Primeiramente temos o INT que se refere aos números inteiros. Ex: 7, -9, 0, 1, -1

n1 = int(input('Digite um número: '))
print(type(n1))

#FLOAT - refere-se aos números reais, que possuem vírgula ou ponto flutuante. Ex: 7.0, 15.2645, -14.235352

n2 = float(input('Digite um número: '))
print(type(n2))

#BOOL - refere-se aos valores booleanos, que são apenas True ou False

n3 = bool(input('Digite um valor: '))
print(type(n3))

#STR - refere-se às palavras e caracteres
texto = str(input('Digite uma palavra: '))
print(type(texto))

#Como verificar se o valor digitado é numérico ou não

valor = input('Digite aluma coisa: ')
print(valor.isnumeric())

#Como verificar se o valor digitado é letra

valor1 = input('Digite um valor: ')
print(valor1.isalpha())

#Como verificar se o valor digitado é alphanumerico

valor2 = input('Digite um valor: ')
print(valor2.isalnum())

#Como verificar se o valor digitado esta em maiúsculo

valor3 = input('Digite um valor: ')
print(valor3.isupper())

#Como verificar se o valor digitado esta em minúsculo

valor4 = input('Digite um valor: ')
print(valor4.islower())

#Verificação se a string possui apenas espaços em branco ou tabulações

valor5 = input('Digite um valor: ')
print(valor5.isspace())

#Verificação se os caracteres da string são imprimíveis

valor6 = input('Digite um valor: ')
print(valor6.isprintable())

#Vefificação se a string tem identificadores válidos para com as regras da linguagem
#Regras
#Deve começar com uma letra (maiúscula ou minúscula) ou com um caractere de sublinhado (_).
#Os caracteres subsequentes podem ser letras, dígitos numéricos ou caracteres de sublinhado.
#Não pode conter espaços ou caracteres especiais, exceto sublinhados.
#Não pode ser uma palavra-chave reservada da linguagem.

valor7 = input('Digite um valor: ')
print(valor7.isidentifier())

#Verificação se a string possui todos os caracteres dentro do ASCII

valor8 = input('Digite um valor: ')
print(valor8.isascii())

#Verificação se todos os caracteres da string contém apenas números

valor9 = input('Digite um valor: ')
print(valor9.isdecimal())

#Verificação se a string está em formato de título, ou seja, começa as palavras começam em maiúsculo e o resto é tudo minúsculo

valor10 = input('Digite um valor: ')
print(valor10.istitle())