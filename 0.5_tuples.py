### Tuples ### No se puede modificar el contenido de las tuplas

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (14, 1.83, "Jose Juan", "Lara", "Lara")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[4]) IndexError
# print(my_tuple[-6]) IndexError

print(my_tuple.count("Lara"))
print(my_tuple.index("Jose Juan"))
print(my_tuple.index(14))

# my_tuple[1] = 2.00 TypeError: 'tuple' object does not support item assignment

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6])

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = "Giottos33"
my_tuple.insert(1, "Azul")
my_tuple = tuple(my_tuple)
print(type(my_tuple))
print(my_tuple)

# del my_tuple[2] TypeError: 'tuple' object doesn't support item deletion

del my_tuple
# print(my_tuple) NameError: name 'my_tuple' is not defined