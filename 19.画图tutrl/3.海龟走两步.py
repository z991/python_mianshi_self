import turtle


def draw_art():
    window = turtle.Screen()
    window.bgcolor("blue")
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("orange")
    brad.speed('fast')


    brad.forward(100)
    brad.right(45)
    brad.forward(100)
    brad.right(135)
    window.exitonclick()


draw_art()