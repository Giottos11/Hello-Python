### Sets ###

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))

my_other_set = {"Jose Juan", "Lara", 14}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add("Giottos33")

print(my_other_set) # Un set no es una estructura ordenada.

my_other_set.add("Giottos33") # Un set no admite repetidos.

print(my_other_set)

print("Lara" in my_other_set)
print("Laron" in my_other_set)

my_other_set.remove("Lara")
print(my_other_set)

my_other_set.clear()
print(my_other_set)

del my_other_set
# print(my_other_set) NameError: name 'my_other_set' is not defined