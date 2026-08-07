password = input("Escribe tu contraseña:")

if password == "":
    print("Tines que escribir algo")

elif len(password) < 8:
    print("Tu contraseña es muy corta")

else:
    tiene_numero = False

    for letra in password:
        if letra.isdigit():
            tiene_numero = True

    if tiene_numero:
        tiene_letra = False

        for letra in password:
            if letra.isalpha():
                tiene_letra = True

        if tiene_letra:
            print("Tu contraseña es aceptable")
        else:
            print("Tu contraseña necesita una letra")
    else:
        print("Tu contraseña necesita un numero")