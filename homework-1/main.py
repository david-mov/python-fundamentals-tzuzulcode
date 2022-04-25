# 1. Dados dos números enteros almacenados en dos variables, imprime su producto solo si el producto es mayor que 1000. 
# Si el producto es menor a 1000, imprime su suma.

def biggerThanAThousand(num1, num2):
    if num1 * num2 > 1000:
        result = num1 * num2
    else:
        result = num1 + num2
    print(f'Result: {result}')

# 2. Dada una variable 'minutos' que almacena un número entero, realiza un programa que lo convierta a segundos.

def minutesToSeconds(minutes):
    print(f'Result: {minutes * 60} seconds')

# 3. Teniendo tres variables, 'lado1', 'lado2' y 'lado3' de un triangulo, escribe un programa que calcule el perimetro y área. 
# Además de verificar si es un triangulo isosceles, escaleno o equilatero.

def triangleCalculator(side1, side2, side3):
    if side1 == side2 and side2 == side3:
        print("It's a equilateral triangle")
        height = ( side1 * pow(3, (1/3)) ) / 2
    elif side1 != side2 and side2 != side3 and side3 != side1:
        print("It's a scalene triangle")
        s = (side1 + side2 + side3) / 2
        height = (2 / side1) * pow(s*(s-side1)*(s-side2)*(s-side3), 0,5)
    else:
        print ("It's a isosceles triangle")
        height = pow(pow(side1, 2) - (pow(side2, 2) / 4), 0,5)
    print(f'The triangle area is {side1 * height / 2}')
    print(f'The triangle perimeter is {side1 + side2 + side3}')

print('Calculate result according to the product')
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))
biggerThanAThousand(num1, num2)

print('Convert minutes to seconds')
minutes = int(input('Enter a number of minutes without decimals: '))
minutesToSeconds(minutes)

print('Calculate triangle type and properties')
side1 = int(input('Enter the triangle base length: '))
side2 = int(input('Enter the length of one side of the triangle: '))
side3 = int(input('Enter the length of the other side of the triangle: '))
triangleCalculator(side1, side2, side3)