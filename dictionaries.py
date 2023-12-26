#Definicion de diccionarios
product ={
    "name": "book",
    "quantity": 3,
    "price": 4.99
}

person ={
    "first_name": "ryan",
    "last_name": "ryan"
}


print(type(product))
print(type(person))

#imprimir el nombre de las keys del diccionario
print(person.keys())

#imprimir tanto keys como valores en el diccionario
print(person.values())

#limpiar diccionario
person.clear
print(person)

#prueva de lista llena de diccionarios
products = [
    {"name": "book", "price" : 10.99},
    {"name": "laptop", "price" : 100.0}

]
print(products)


#borrar diccionario
del person
print(person)
