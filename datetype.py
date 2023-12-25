#Cuatro formas "distintas" de definir strings

#Una vez coma simple o coma doble

print('Hello world')
print("Hello world")

#Tres veces coma simple o coma doble
print('''Hello world''')
print("""Hello world""")

#Imprime "Class str" ya que imprime el tipo de dato que es 
print(type("Hello world"))

#Concatenar cadenas de texto y numero
print("Bye"+"World")

#Hacer uso de numeros
#Tipo entero
print(type(30))

#tipo float
print(type(30.1))

#Uso de banderas(Boolean)
#activado
print(type(True))

#Desactivado
print(type(False))

#Listas
[10,20,30,11]
["Hello", "Hola", "Hi", "Buenas"]
["Hello", 10, "Hola", 30, "Hi", 20, "Buenas", 11]

print(type([10,20,30,11]))

#Tuplas(Son inmutables)
(10,20,30,11)
print(type((10,20,30,11)))

#Diccionarios
print(type({
    "name":"Johan",
    "lastname":"Ontiveros",
    "nickname":"Homi12"
}))

#Tipo de dato sin definir
print(type(None))