
demo_list = [1, 'hello', 1.34, True, [1,2,3]]
colors = ['red', 'green', 'blue']

#llenar lista con una tupla
numers_list = list((1, 2, 3, 4))

#range sirve para llenar una lista con un rango determinado de valores
r = list(range(1, 100))
print(r)

#imprime el tipo de la variable
print(type(colors))

#imprime el tampaño del arreglo
print(len(demo_list))

#imprime un valor de la lista
print(colors[1])
print(colors[-1])

#buscar si un dato existe en un arreglo y devuelve booleano
print("green" in colors)

#sirve para agregar elementos al arreglo, pero no se puede agregar mas de uno a la vez
colors.append('violet')
colors.append(('yellow', 'brown'))

#Agrega datos a la lista y si puede agregar varios
colors.extend(['yellow', 'brown'])

#insertar en un lugar determinado de la lista
colors.insert(1, 'pink')

#Eliminamos el ultimo dato de la lista o damos el index del dato a eliminar
colors.pop()
print(colors)

#Ordenamos los items de la lista por orden alfabetico
colors.sort()
print(colors)

#Ordenamos los items de la lista por orden alfabetico inverso
colors.sort(reverse=True)
print(colors)

#buscamos el index de un dato especifico
print(colors.index('red'))

#contamos cuantas veces aparece un dato en la lista
print(colors.count('red'))

#Eliminamos todos los items de la lista
colors.clear()

colors.append('Black')
print(colors)

