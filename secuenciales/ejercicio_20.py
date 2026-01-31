e2 = int(input("Monedas de 2€: "))
e1 = int(input("Monedas de 1€: "))
c50 = int(input("Monedas de 50c: "))
c20 = int(input("Monedas de 20c: "))
c10 = int(input("Monedas de 10c: "))

euros = e2 * 2 + e1 + (c50 * 50 + c20 * 20 + c10 * 10) // 100
centimos = (c50 * 50 + c20 * 20 + c10 * 10) % 100

print(euros, "€ y", centimos, "céntimos")