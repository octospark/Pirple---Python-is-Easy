''' Below I'm using the turtle and random modules to simulate two types
of random walk. A random walk is a path that starts from a given point
and makes a choice for each subsequent step regarding the direction
and/or the length of the step.
'''

import turtle, random

def randomWalkGrid(steps=200, stepSize=20):
    for step in range(steps):
        direction = random.randint(0, 3)
        if direction == 0:
            turtle.setheading(0)
            turtle.forward(stepSize)
        elif direction == 1:
            turtle.setheading(270)
            turtle.forward(stepSize)
        elif direction == 2:
            turtle.setheading(180)
            turtle.forward(stepSize)
        else:
            turtle.setheading(90)
            turtle.forward(stepSize)
    turtle.mainloop()


def pureRandomWalk(steps=200):
    for step in range(steps):
        length = random.randint(10, 30)
        direction = random.randint(0, 360)
        turtle.setheading(direction)
        turtle.forward(length)
    
    turtle.mainloop()



choice = input("Do you want a pure random walk(0) or a grid random walk(1): ?")
if choice == '0':
    pureRandomWalk()
else:
    randomWalkGrid()
