"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.

"""

from random import randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
indicador = 0 

print("¡Bienvenido al juego snake!")
print("\nElige la velocidad (Baja, Media, Alta): ")
velocidad = input()

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y


def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)
    global indicador
    
    if  (head in snake):
        if (indicador == 0):
            square(head.x, head.y, 9, 'red')
            update()
            return
        else:
            indicador = 0
    elif not inside(head):
        if (not (head.y < 190)):
            indicador = 1
            for i in snake:
                change(0, -9)
                change(0, -9)
            change(0, -10)
        elif (not (-200 < head.y)):
            indicador = 1
            for i in snake:
                change(0, 9)
                change(0, 9)
            change(0, 10)
        elif (not (head.x < 190)):
            indicador = 1
            for i in snake:
                change(-9, 0)
                change(-9, 0)
            change(-10, 0)
        elif (not (-200 < head.x)):
            indicador = 1
            for i in snake:
                change(9, 0)
                change(9, 0)
            change(10, 0)


    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    if (velocidad == "Baja"):
        ontimer(move, 200)
    elif (velocidad == "Media"):
        ontimer(move, 100)
    elif (velocidad == "Alta"):
        ontimer(move, 50)
    else:
        ontimer(move,150)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
