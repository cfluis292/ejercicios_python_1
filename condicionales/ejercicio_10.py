import math

x1 = float(input("x1: "))
y1 = float(input("y1: "))
r1 = float(input("r1: "))
x2 = float(input("x2: "))
y2 = float(input("y2: "))
r2 = float(input("r2: "))

distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

if distancia == 0:
    print("concéntricas")
elif distancia > r1 + r2:
    print("exteriores")
elif distancia == r1 + r2:
    print("tangentes exteriores")
elif distancia > abs(r1 - r2):
    print("secantes")
elif distancia == abs(r1 - r2):
    print("tangentes interiores")
else:
    print("interiores")