# Entendendo os dados da variável:

resp = input('Digite algo: ')
print('O tipo primitivo do que você digitou é: ', type(resp))
print('É uma palavra: ', resp.isalpha())
print('É um número: ', resp.isnumeric())
print('Tem apenas letras maiúsculas: ', resp.isupper())
print('Tem apenas letras minúsculas: ', resp.islower())
print('Tem letras e números:', resp.isalnum())
print('Está em branco: ', resp.isspace())
