import turtle
import random 

turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()

def quadrado():
    turtle1.speed(10)
    turtle.bgcolor("red")
    for i in range(10):
        turtle1.forward(random.randint(1,200))
        turtle1.right(random.randint(1,360))

def triangulo():
    turtle2.speed(10)
    for x in range(10):
        turtle2.forward(random.randint(1,200))
        turtle2.right(random.randint(1,360))
        
quadrado()
triangulo()
