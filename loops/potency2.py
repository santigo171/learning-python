# ciclo while

def run(number, limit):
    potency = 0
    result = number ** potency
    while result <= limit:
        print(str(number) + "^" + str(potency) +
              " = " + str(result))
        potency = potency + 1
        result = number ** potency


if __name__ == "__main__":
    number = int(input("Qué número quieres elevar? "))
    limit = int(input("A que número limite quieres llegar? "))
    run(number, limit)
