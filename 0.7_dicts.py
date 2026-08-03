### Dictionaries ###

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Jose", "Apellido":"Lara", "Edad":200, 1:"Python"}

my_dict = {
    "Nombre":"Jose", 
    "Apellido":"Lara",
    "Edad":200,
    "Lenguajes": {"Python", "Swift", "Kotlin"},
    1:1.77
    }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])

my_dict["Nombre"] = "Brais"
print(my_dict["Nombre"])

print(my_dict[1])

my_dict["Calle"] = "Calle Giottos"
print(my_dict)

del my_dict["Calle"]
print(my_dict)

print("Jose" in my_dict)
print("Apellido" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["Nombre", 1, "Piso"]

my_new_dict = dict.fromkeys(my_list)
print(my_new_dict)
my_new_dict = dict.fromkeys(("Nombre", 1, "Piso"))
print(my_new_dict)
my_new_dict = dict.fromkeys(my_dict)
print((my_new_dict))
my_new_dict = dict.fromkeys(my_dict, "Mouredev")
print((my_new_dict))