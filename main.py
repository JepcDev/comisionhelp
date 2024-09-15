#se puede almacenar string
#nombre = "Jose"
#print(nombre)

#nombre = "Juan"
#print(nombre)

#se puede almacenar numeros
#edad = 30
#print(edad)

#edad2 = 10
#print(edad + edad2)

#ALmacena datos obtenidos de un input
#nombre = input("Dime tu nombre: ")
#print("Tu nombre es " + nombre)

#Alamacena datos de dos variables
#nombre = "Hola"
#nombre2 = "Python"
#frase = nombre + " " + nombre2
#print(frase)

#alamcena resultados de operaciones aritmeticas y demas
#edad = 20
#edad2 = 10
#edadtotal = edad + edad2
#print(edadtotal)

#Integer y floats
#print("INTEGERS")
#mi_numero = 1 + 3

#print(mi_numero + mi_numero)
#print(mi_numero)
#print(type(mi_numero))

#print("\nFLOATS")
#mi_numero = 5.8

#print(mi_numero)
#print(type(mi_numero))

#hay que convertir todo lo que se recive del input a un tipo de dato con el cual se pueda trabajar y hacer operaciones matematicas calculos ect
#edad = input("Dime tu edad: ")
#print(edad)

#print(type(edad))


#Practica
#num1 = 7.5
#num2 = 2.5

#suma_numero = num1 + num2
#print(suma_numero)
#print(type(suma_numero))

#Conversiones
#Conversion implicita
#num1 = 20
#num2 = 30.1
#print(type(num1))
#num1 = num1 + num2
#print(type(num1))
#print(type(num2))

#Conversion explicita
#num1 = 5.8
#print(num1)
#print(type(num1))

#num2 = int(num1)
#print(num2)
#print(type(num2))

#Solucion
edad= input("Dime tu edad: ")
print(type(edad))
edad = int(edad)
print(type(edad))
nueva_edad = 1 + edad
print("Tu edad va a ser :" + str(nueva_edad))