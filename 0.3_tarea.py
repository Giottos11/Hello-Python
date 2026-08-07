password = input("Escribe tu contraseña:")

if password == "":
    print("Tines que escribir algo")

elif len(password) < 8:
    print("Tu contraseña es muy corta")

else:
    tiene_numero = False
    tiene_letra = False
    tiene_minuscula = False
    tiene_mayuscula = False

    for letra in password:
        if letra.isdigit():
            tiene_numero = True
        if letra.isalpha():
            tiene_letra = True
            if letra.islower():
              tiene_minuscula = True
            if letra.isupper():
                tiene_mayuscula = True

    if tiene_numero and tiene_letra and tiene_minuscula and tiene_mayuscula:
        print("Tu contraseña es aceptable")

    elif not tiene_numero:
        print("Tu contraseña necesita al menos un numero")

    elif not tiene_letra:
        print("Tu contraseña necesita una letra")

    elif not tiene_minuscula:
        print("Tu contraseña necesita una letra en minuscula")

    else:
        print("Tu contraseña necesita una letra en mayuscula")