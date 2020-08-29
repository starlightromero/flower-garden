"""Import Turle Graphics, Random, Flower, Tree, and Bush."""
import turtle as jerry
from random import choice, randint
from Flower import Flower
from Tree import Tree
from Bush import Bush

colors = ["pink", "green", "red", "blue", "yellow", "purple"]

jerry.speed(10)
screen = jerry.Screen()
screen.setup(800, 800)

for _ in range(3):
    flower = Flower(
        randint(-200, 200), randint(-200, 200), randint(5, 20), choice(colors)
    )
    flower.draw()
    tree = Tree(
        randint(-200, 200), randint(-200, 200), randint(7, 12), choice(colors)
    )
    tree.draw()
    bush = Bush(
        randint(-200, 200), randint(-200, 200), randint(5, 10), choice(colors)
    )
    bush.draw()


def goto_clicked(x, y):
    """Change pencolor and go to x, y coordinates."""
    jerry.pencolor(choice(colors))
    jerry.goto(x, y)


def goto_dragged(x, y):
    """Set Jerry's heading direction and go to x, y coordinates."""
    jerry.setheading(jerry.towards(x, y))
    jerry.goto(x, y)


screen.onclick(goto_clicked)
jerry.ondrag(goto_dragged)

jerry.done()
