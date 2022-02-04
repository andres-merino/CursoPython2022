# Inicio de programa
print("Introducir los coeficientes de la ecuación ax^2+bx+c=0.")
# Lectura de datos
a = input("a = ")
b = input("b = ")
c = input("c = ")
# Conversión a enteros
a = int(a)
b = int(b)
c = int(c)
# Cálculo de soluciones
x1 = (-b+(4*a*c-b**a)**(1/2))/(2*a)
x2 = (-b-(4*a*c-b**a)**(1/2))/(2*a)
# Impresión de soluciones
print("Las respuestas son:", x1, "y", x2)
