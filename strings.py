#Uso de variables
myStr = "Hello World Car e"

#Con myStr podemos ver que podemos hacer con esa variable
print(dir(myStr))

#todas mayusculas
print(myStr.upper())

#todas minusculas
print(myStr.lower())

#Invierte mayusculas y minusculas
print(myStr.swapcase())

#Mayuscula solo la primer letra
print(myStr.capitalize())

#intercambiar un una parte de la cadena de texto por otra
print(myStr.replace("Hello", "bye"))

#contar cuantos caracteres como el buscado hay en la cadena
print(myStr.count(' '))

#Devuelve True si inicia con los caracteres buscados la cadena de texto
print(myStr.startswith('He'))

#Devuelve True si termina con los caracteres buscados la cadena de texto
print(myStr.endswith('Car'))

#Divide la cadena de texto por espacios
print(myStr.split(' '))

#Busca un caracter en especifico en la cadena de texto y devuelve cuantas veces existe
print(myStr.find("o"))

#Imprime el tamaño completo del arreglo "generado" por la cadena de texto
print(len(myStr))

#encuentra el valor y devuelve en que posicion se encuentra por primera vez en la cadena de texto
print(myStr.index('e'))

#Comprueva si es numerico o no y devuelve una bandera o boolean
print(myStr.isnumeric())

#Comprueva si es alphanumerico
print(myStr.isalpha())

#Imprime el valor en la posicion indicada, si ponemos un numero negativo sera elegido 
#de la cadena de texto en orden de izquierda a derecha si ponemos -1 nos dara el ultimo valor del string
print(myStr[4])

#formas de concatenar una variable
nStr = Johan

print("My name is " + nStr)

print(f"My name is {nStr}")

print("My name is {nStr}".format(nStr))