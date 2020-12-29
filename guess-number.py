import random

GREEN = '\033[32m'
YELLOW = '\033[33m'
RED = '\033[31m'
RESET = '\033[39m'


def is_number_valid(number, limit):
    if limit < number:
        print(
            f"\n{number} es un número mayor que {limit} -_-, ingresa un número válido porfavor")
    elif number < 1:
        print(
            f"\n{number} es un número menor que 1 -_-, ingresa un número válido porfavor")
    else:
        return True


def game(number, limit, difficulty):
    random_number = random.randint(1, limit)
    while number != random_number:
        if number > random_number:
            number = int(input(f"Ingresa un número menor que {number}: "))
        elif number < random_number:
            number = int(input(f"Ingresa un número mayor que {number}: "))

    print("\nFelicidades!!!, el número era " + str(random_number) +
          ", ganaste en dificultad" + difficulty + ".")


def game_3(number, limit, difficulty):
    random_number = random.randint(1, limit)
    attempts = 2
    while number != random_number and attempts <= 8:
        if number > random_number:
            number = int(
                input(f"(Intento #{attempts})Ingresa un número menor que {number}: "))
            attempts += 1
        elif number < random_number:
            number = int(
                input(f"(Intento #{attempts})Ingresa un número mayor que {number}: "))
            attempts += 1
    if number == random_number:
        print("\nFelicidades!!!, el número era " + str(random_number) +
              ", ganaste en dificultad" + difficulty + ".")
    else:
        print("\nPerdiste, te quedaste sin intentos ￣へ￣, el número era " +
              str(random_number) + ".")


def run():
    menu = "\nBienvenid@ al campo de batalla, donde se derrama SANGRE!!!, tendrás que adivinar el número." + \
        GREEN + "\n\n1. noob" + YELLOW + "  2. Pro" + RED + \
        "   3. ULTRA MEGA PRO" + RESET + "\n\nElige la dificultad del juego: "
    option = int(input(menu))

    if option == 1:
        limit = 100
        difficulty = GREEN + " noob" + RESET
        number = int(
            input(f"\nOk{difficulty}, tienes intentos infinitos, dame un número{GREEN} del 1 al 100: {RESET}"))
        if is_number_valid(number, limit) == True:
            game(number, limit, difficulty)
    elif option == 2:
        limit = 1000
        difficulty = YELLOW + " pro" + RESET
        number = int(
            input(f"\nOk{difficulty}, tienes intentos infinitos, dame un número{YELLOW} del 1 al 1000: {RESET}"))
        if is_number_valid(number, limit) == True:
            game(number, limit, difficulty)
    elif option == 3:
        limit = 1000
        difficulty = RED + " ULTRA MEGA PRO" + RESET
        number = int(
            input(f"\nOk{difficulty}, tienes 8 intentos, dame un número{RED} del 1 al 1000{RESET} (intento #1): "))
        if is_number_valid(number, limit) == True:
            game_3(number, limit, difficulty)
    else:
        print("Escibre una opción válida porfavor.")

    print("\n\nProducto creado por David Hurtado @santigo171")


if __name__ == "__main__":
    run()
