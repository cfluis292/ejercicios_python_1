My_list = [3, 5, 7, 8, 1, 5, 2]
print(My_list)
print(type(My_list))

print(My_list[0])
print(My_list[3])
print(My_list[-1])

print(len(My_list))

my_other_list = ["hi", True, 1, 1.3, [10, 11]]
print(my_other_list[4][0])

for i in range(len(my_other_list)):
    print(i, "->", my_other_list[i])

for i in my_other_list:
    print(i)

numbers = [3, 1, 6, 4, 8, 9, 5, 2]
print(numbers)
numbers.append(15) #Insertar un nuevo elemento al final de la lista
numbers.append(53)
print(numbers)
numbers.pop() #Extraer el último elemento de la lista
print(numbers)
numbers.reverse() #Invertir el orden de los elementos de la lista
print(numbers)
numbers.sort() #Ordenar los elementos de la lista
print(numbers)
numbers.clear() 
print(numbers)