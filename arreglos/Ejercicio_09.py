t_minimas = []
t_maximas = []

for i in range(1, 6):
    t_minimas.append(float(input(f"Día {i} - Mínima: ")))
    t_maximas.append(float(input(f"Día {i} - Máxima: ")))

print("\nTemperaturas medias")
for i in range(5):
    media = (t_minimas[i] + t_maximas[i]) / 2
    print(f"Día {i+1}: {media}")

min_global = min(t_minimas)
print("\nDías con menos temperatura")
for i in range(5):
    if t_minimas[i] == min_global:
        print(f"Día {i+1}")

buscada = float(input("\nBuscar temperatura máxima: "))

if buscada in t_maximas:
    for i in range(5):
        if t_maximas[i] == buscada:
            print(f"Día {i+1}")
else:
    print("No hay ningún día con esa temperatura.")