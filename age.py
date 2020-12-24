print("")  # Esto lo puse para que en la terminal haya un pequeño espacio arriba de la pregunta (se ve mas bonito)

edad = int(input("Escribe tu edad: "))
print("")

if edad > 122:
    edad = str(edad)
    print("Tienes " + edad + " años, es decir, eres MAYOR DE EDAD, de hecho, tienes el record de la persona más longeva del mundo (Superaste a Jeanne Louise Calment).")

elif edad > 17:
    edad = str(edad)
    print("Tienes " + edad + " años, es decir, eres MAYOR DE EDAD.")

elif edad < 0:
    edad = str(edad)
    print("Tienes " + edad + " años, es decir, ni siquiera has nacido.")

else:
    edad = str(edad)
    print("Tienes " + edad + " años, es decir, ERES MENOR DE EDAD.")
