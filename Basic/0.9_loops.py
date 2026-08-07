### Loops ###

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1
else: # Es opcional
    print("¡¡Boom!!")

print("La ejecución continúa")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecucuión")
        break
    print(my_condition)

print("La ejecución continúa")

# For

my_list = [35, 24, 62, 52, 30, 17]

for element in my_list:
    print(element)

my_tuple = (14, 1.83, "Jose Juan", "Lara", "Lara")

for element in my_tuple:
    print(element)

my_set = {"Jose Juan", "Lara", 14}

for element in my_set:
    print(element)

my_dict = {"Nombre":"Jose", "Apellido":"Lara", "Edad":200, 1:"Python"}

for element in my_dict: # Para que sean de los elementos list(my_dict.values())
    print(element)
    if element == "Edad":
        break
else:
    print("El bucle for para diccionario ha finalizado")

print("La ejecución continúa")

for element in my_dict: # Para que sean de los elementos list(my_dict.values())
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")
else:
    print("El bucle for para diccionario ha finalizado")