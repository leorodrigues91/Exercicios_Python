char = input('Digite algo: ')
print(f'O tipo primitivo de {char} é:', type(char))
print('Só tem espaços?', char.isspace())
print('É somente numérico?', char.isnumeric())
print('É somente alfabético?', char.isalpha())
print('É alfanumérico?', char.isalnum())
print('Está totalmente em maiúsculas?', char.isupper())
print('Está totalmente em minúsculas?', char.islower())
print('Está capitalizada?', char.istitle())
