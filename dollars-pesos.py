dollar = input("Cuantos dolares tienes?: ")
dollar = float(dollar)
peso_value = 0.00029
pesos = dollar / peso_value
pesos = round(pesos, 2)
pesos = str(pesos)
print("Tienes $" + pesos + " pesos colombianos")
