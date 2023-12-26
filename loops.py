#definicion de una lista
foods = ["apples", "bread", "chesse", "milk", "bananas", "graves"]

#imprimir todos los datos de la lista y cuando encuentre cierto dato hacer ciertas instrucciones
#y denetener el for con el break
for food in foods:
    if food == "chesse":
        print("you have to buy this")
        break
    print(food)

#imprime todos los datos pero al realizar la validación omite el imprimir el dato deseado
#haciendo uso de continue
for food in foods:
    if food == "chesse":
        print("you have to buy this")
        continue
    print(food)

#for en un determinado rango de numeros
for number in range (0, 8):
    print(number)

#for que itera cada letra de la cadena de texto
for letter in "Hello":
    print(letter)

#uso de while(ciclo condicional)
count = 4
while count <= 10:
    print(count)
    count = count+1

