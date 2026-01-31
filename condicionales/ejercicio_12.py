ao = int(input("Año: "))

if (ao % 4 == 0 and ao % 100 != 0) or ao % 400 == 0:
    print("Bisiesto")
else:
    print("No bisiesto")