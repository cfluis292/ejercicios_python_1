# pero en orden inverso, y muéstralo por la pantal

vector = []
vector_reverse = []

for i in range(1, 6):
    num = input(f'Inserta cadena de texto [{i}]: ')
    vector.append(num)

for i in range(4, -1, -1):
    vector_reverse.append(vector[i])

print(vector)
print(vector_reverse)