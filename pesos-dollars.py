pesos = input("Cuantos pesos colombianos tienes?: ")
pesos = float(pesos)
dollar_value = 3500
dollars = pesos / dollar_value
dollars = round(dollars, 2)
dollars = str(dollars)
print("Tienes $" + dollars + " dólares")