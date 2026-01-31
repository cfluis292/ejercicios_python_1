alumnos = int(input("Alumnos: "))

if alumnos >= 100:
    por_alumno = 65
elif alumnos >= 50:
    por_alumno = 70
elif alumnos >= 30:
    por_alumno = 95
else:
    por_alumno = 4000 / alumnos if alumnos > 0 else 0

if alumnos > 0:
    total = alumnos * por_alumno if alumnos >= 30 else 4000
    print("Autobús: ", total)
    print("Cada alumno: ", por_alumno:.2f)
else:
    print("Error: número de alumnos no válido")