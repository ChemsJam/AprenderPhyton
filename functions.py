#definimos una funcion basica
def hello():
    print("Hello world")
hello()

#funcion que imprime el nombre o si no recibe datos ya tiene dato preestablecido
def hello1(name="Person"):
    print("Hello " + name)

hello1("joe")
hello1("ryan")
hello1("fazt")
hello1()

#
def add(numberOne, numberTwo):
    return print(numberOne + numberTwo)

add(10,30)
add(600,10)

addlam = lambda numberOne, numberTwo: numberOne + numberTwo

print(addlam(10,30))
    