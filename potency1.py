def run(number, limit, potency):
    result = number ** potency
    if result <= limit:
        print(str(number) + "^" +
              str(potency) + " = " + str(result))
        run(number, limit, potency + 1)
    else:
        print("Fin")

    result = number ** potency


if __name__ == "__main__":
    number = int(input("Qué número quieres elevar? "))
    limit = int(input("A que número limite quieres llegar? "))
    run(number, limit, 0)
