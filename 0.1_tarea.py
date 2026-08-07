password = input("Escribe tu contraseña: ")

if password == "":
    print("Tienes que escribir una contraseña")

elif len(password) < 8:
    print("Tu contraseña es débil")

else:
    tiene_numero = False

    for letra in password:
        if letra.isdigit():
            tiene_numero = True

    if tiene_numero:
        print("Tu contraseña es aceptable")
    else:
        print("Tu contraseña necesita un número")