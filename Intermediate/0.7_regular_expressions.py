### Regular Expressions ###

import re

my_string = "Esta es la lección 7: Expresiones Regulares"
my_other_string = "Esta no es la lección 6: Manejo de Ficheros"

match = re.match("Esta es la lección", my_string, re.I)
print(match)
print(match.span())

print(re.match("Esta es la lección", my_other_string))
print(re.match("Expresiones Regulares", my_string))