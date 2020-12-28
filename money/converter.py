YELLOW = "\033[33m"
BLUE = "\033[36m"
RESET = "\033[39m"

menu = """
(☞ﾟヮﾟ)☞ Bienvenid@ a este conversor de monedas. 😎💸💰💵

Hecho por David Hurtado

    1 - Pesos colombianos  --> DOLARES
    2 - Pesos mexicanos    --> DOLARES
    3 - Pesos argentinos   --> DOLARES
    4 - Soles peruanos     --> DOLARES
    5 - Bolivianos         --> DOLARES
    6 - Euros              --> DOLARES
    7 - Pesos chilenos     --> DOLARES
    8 - Reales brasileños  --> DOLARES

    0 - Salir del menú

Elige una opción: """

option = float(input(menu))

print("")


def conversion(currency_name, dollar_value):
    bagde = float(input("Cuantos " + BLUE + currency_name +
                        RESET + " tienes?: " + BLUE))
    dollars = bagde / dollar_value
    dollars = round(dollars, 2)
    bagde = str(bagde)
    dollars = str(dollars)
    print("")
    print(RESET + "Tienes " + YELLOW + dollars + " dólares" + RESET +
          ", es decir " + BLUE + bagde + " " + currency_name + RESET + ".")


if option == 1:
    conversion("pesos colombianos", 3500)

elif option == 2:
    conversion("pesos mexicanos", 19.92)

elif option == 3:
    conversion("pesos argentinos", 83.28)

elif option == 4:
    conversion("soles peruanos", 3.61)

elif option == 5:
    conversion("bolivianos", 6.93)

elif option == 6:
    conversion("euros", 0.82)

elif option == 7:
    conversion("pesos chilenos", 714.80)

elif option == 8:
    conversion("reales brasileños", 5.22)

elif option == 0:
    print("A bueno adiós master.")

else:
    print("Por favor ingresa " + BLUE + "una opción correcta" +
          RESET + " (Pon solo el número). ")
