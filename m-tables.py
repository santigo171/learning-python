def table(number):
    print(f"\nEsta es la tabla del {number}")
    for counter in range(1, 11):
        product = number * int(counter)
        print(f"{number} X {counter} = {product}")


def run():
    number = int(
        input("\nIngrese un número para darle la tabla de multiplicar: "))
    table(number)


if __name__ == "__main__":
    run()
