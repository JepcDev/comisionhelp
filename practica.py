#PRACTICA
#VARIABLES
#1
nombre = "Tony Soprano"
edad = 51
#2
nombre = "Julia"
apellido = "Robets"
nombre_completo = nombre + " " + apellido
print(nombre_completo)
#3
curso = "Python"
print("Estas tomando un curso de " + curso)

#Integer
#1
num_entero = 11
print(num_entero)
print(type(num_entero))

#FLOAT
#1
num_decimal = 11.1
print(num_decimal)
print(type(num_decimal))

#TIPOS DE DATOS NUMERICOS
#1
num1 = 7.5
num2 = 2.5
print(type(num1+num2))

#CONVERSIONES
#1
num1 = 7.5
print(num1)
print(type(num1))
num1 = int(num1)
print(num1)
print(type(num1))
#2
num2 = 10
print(num2)
print(type(num2))
num2 = float(num2)
print(num2)
print(type(num2))
#3
num1 = "7.5"
num2 = "10"
print(float(num1) + float(num2))

#FORMATEAR CADENAS
#1
nombre_asociado = "Jesse Pinkman"
numero_asociado = "399058"
print(f"Estimado/a {nombre_asociado}, su número de asociado es: {numero_asociado}")
#2
puntos_nuevos = 350
puntos_totales = 1225
print(f"Has ganados {puntos_nuevos} puntos! en total, acumulas {puntos_totales} puntos")
#3
puntos_anteriores = 875
puntos_nuevos = 350
print(f"Has ganado {puntos_nuevos} puntos! en total, acumulas {puntos_anteriores+puntos_nuevos} puntos")

#OPERADORES MATEMATICOS
#1
num1 = 874
num2 = 27
print(num1//num2)
#2
num1 = 456
num2 = 33
print(num1%num2)
#3
print(783**0.5)

#REDONDEO
#1
print(round(10/3,2))
#2
valor = 10.676767
print(round(valor))
#3
print(round(5**0.5,4))

