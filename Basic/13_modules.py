### Modules ###

import Basic.my_module as my_module

my_module.sumValue(5, 3, 1)
my_module.printValue("Hola Python")

from Basic.my_module import sumValue, printValue

sumValue(5, 3, 1)
printValue("Hola Python")

import math

print(math.pi)
print(math.pow(2, 8))

from math import pi as py_value

print(py_value)