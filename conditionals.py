#los condicionales coomparan y retornan un valor True o False dependiendo del caso
x = 40
y = 20
if x < 30:
    print(f"{x} is less than 30")
else:
    print(f"{x} is more than 30")

color = "red"

if color == "red":
    print("the color is red")
elif color == "blue":
    print("The color is blue")
else:
    print("Another color")

name = "Johan"
lastname = "Ontiveros"

#condicionales anidadas de texto
if name =="Johan":
    if lastname == "Ontiveros":
        print("You are Johan Alejandro")
    else:
        print("You are not Johan Alejandro")
else:
    print("You are not Johan")

#condicionales con operadores logicos
    
if x > 2 and x <= 10 :
    print("x is greater than two and less than or equal to ten")
if x > 2 or x <= 20:
    print("x is greater than two or less than or equal to twenty")
if (not(x == y)):
    print("X and Y are not equals...")
