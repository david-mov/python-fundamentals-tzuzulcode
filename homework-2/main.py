# 1. Escriba una declaración if que solicite el nombre del usuario a través de la función input(). 
# Si el nombre es "Bond", escriba "Bienvenido a bordo 007". De lo contrario, imprima "Buenos días NOMBRE". 
# (Reemplazar Nombre con el nombre del usuario)

name = input('Enter your name: ')
if name == 'Bond':
    print('Welcome aboard 007')
else:
    print(f'Good morning {name}')

# 2. Muestra un menú con varias opciones y lee la variable 'opcion', imprime la opción seleccionada como 
# 'Seleccionaste la opcion <opcion>'. Si la opción no está en las condiciones, imprime “Opción no válida”.

# Ejemplo
# Seleccione una opción
# 1. Imprimir hola
# 2. Muéstrame un héroe
# 3. Dame la hora
# 4. Salir

import random
from datetime import datetime

menu_options = {
    1: 'Print hello',
    2: 'Show me a hero',
    3: 'Give me the time',
    4: 'Exit',
}

heroes = ['Superman', 'Batman', 'Spider-Man', 'Captain America']

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key])

def option_1():
    print(f'Hello {name}')

def option_2():
    print(random.choice(heroes))

def option_3():
    time = datetime.now().strftime('%H:%M:%S')
    print(f'Current time: {time}')


while(True):
    print_menu()
    option = None
    try:
        option = int(input('Enter your choice: '))
    except:
        print('Wrong input. Please enter a number...')
        continue

    if option == 1: option_1()
    elif option == 2: option_2()
    elif option == 3: option_3()
    elif option == 4:
        print('Thanks message before exiting')
        break
    else:
        print('Invalid option. Please enter a number between 1 and 4.') 


# 3. Siendo d = ( x1  2 + y1  2) ** 0.5
# Leer dos puntos (cuatro variables (una para cada punto) , 'x1' y 'y1').
# Muestra cuál es el punto más cercano al origen. 
# Úselo para determinar la distancia desde el primer punto hasta el origen.


