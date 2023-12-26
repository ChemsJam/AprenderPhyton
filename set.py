#Son "listas" siembargo no están ordenadas, si agregamos datos no será por un orden

#se define con {}
colors = {"Red", "Green", "Blue"}

print(type(colors))
print(colors)

#Buscar si un dato esta en el set
print("Red" in colors)

#añadir al sett
colors.add("Violet")
print(colors)

#Remover del set
colors.remove("Red")
print(colors)

#vaciar set
colors.clear
print(colors)

#eliminar el set o "deletear"
del colors
print(colors)

