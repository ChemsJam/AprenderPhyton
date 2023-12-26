#las tuplas a diferencia de las listas no son modificables
x = (1,2,3,4,5)

print(x[4])

#para eliminar la tupla
del x

#podemos crear un diccionario de datos con las tuplas, siembargo las claves no pueden ser iguales
#ya que si hacemos 2 claves iguales solo imprimira uno de las tuplas

#para poder dar la misma clave a ambos devería definirse como (35.1221, 39.0000): ["Tokyo","New York"] 
locations = {
    (35.1221, 39.0000):"Tokyo",
    (35.1222, 39.0001):"New York"
}
print(locations)