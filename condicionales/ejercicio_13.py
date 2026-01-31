dia = int(input("Dia: "))
mes = int(input("Mes: "))
año = int(input("Año: "))

if mes in [1,3,5,7,8,10,12]:
    mdias = 31
elif mes in [4,6,9,11]:
    mdias = 30
elif mes == 2:
    if (año % 4 == 0 and año % 100 != 0) or año % 400 == 0:
        mdias = 29
    else:
        mdias = 28
else:
    mdias = 0

if mdias != 0 and 1 <= dia <= mdias:
    print("Fecha correcta")
else:
    print("Fecha incorrecta")