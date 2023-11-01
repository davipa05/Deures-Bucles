Número = int(input("Introduce un número cualquiera:"))

factorial = 1
contador = 1

while contador <= Número:
    factorial *= contador
    contador += 1

print(f"El factorial es {factorial}")