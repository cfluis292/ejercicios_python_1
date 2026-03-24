import random

hidden = random.randint(1, 100)
intentos = 1

while intentos <= 10:

    num = int(input('Adivina el número: '))

    if num == hidden:
        print('Adivinaste!')
        print('En', intentos, 'intentos')
        break
    elif num < hidden:
        print('Uno mayor')
    else:
        print('Uno menor')

    intentos += 1

if intentos > 10:
    print("Fallaste XD")
    print("El número era:", hidden)
