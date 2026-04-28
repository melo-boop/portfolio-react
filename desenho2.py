import turtle

def quadrado ():
    turtle.speed(100)
    for i in range(100000000000000):
        turtle.forward(500)
        turtle.right(500)
        turtle.forward(50)
        turtle.right(50)
        turtle.forward(1)
        turtle.right(1)


quadrado()