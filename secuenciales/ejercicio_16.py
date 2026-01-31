v1 = float(input("Velocidad del coche 1 (km/h): "))
v2 = float(input("Velocidad del coche 2 (más pequeña)(km/h): "))
distancia = float(input("Dime la distancia entre los coches (km): "))

thoras = distancia / (v1 - v2)
tminutos = thoras * 60

print("Lo alcanza en", tminutos, "minutos.")