import random
import string


def generate_password():
    mayus = list(string.ascii_uppercase)
    minus = list(string.ascii_lowercase)
    symbols = list(string.punctuation)
    numbers = list(string.digits)

    characters_list = mayus + minus + symbols + numbers

    password = []

    for i in range(15):
        random_character = random.choice(characters_list)
        password.append(random_character)

    password = "".join(password)
    return password


def run():
    password = generate_password()
    print(f"Tu nueva contraseña es: {password}")


if __name__ == '__main__':
    run()
