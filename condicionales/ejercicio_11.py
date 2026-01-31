a = float(input("Lado A: "))
b = float(input("Lado B: "))
c = float(input("Lado C: "))

if a*a + b*b == c*c or b*b + c*c == a*a or c*c + a*a == b*b:
    print("Rectangulo")

if (a == b and a != c) or (b == c and b != a) or (c == a and c != b):
    print("Isosceles")
elif a == b and a == c:
    print("Equilatero")
else:
    print("Escaleno")