def run():
    # for counter in range(10):
    #     if counter % 2 == 1:
    #         continue
    #     print(counter)
    #
    #
    # print("Voy a imprimir solo los numeros pares hasta el "5321")
    # for i in range(10000):
    #     if i == 5321:
    #         break
    #     if i % 2 == 1:
    #         continue
    #     print(i)

    text = str(input("Escribe algo de texto: "))
    # for letter in text:
    #     if letter == "i":
    #         break
    #     print(letter)

    counter = 0
    letter = text[counter]
    while len(text) >= counter:
        letter = text[counter]
        if letter == "m":
            break
        print(letter)
        counter += 1


if __name__ == "__main__":
    run()
