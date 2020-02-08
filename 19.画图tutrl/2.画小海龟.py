import turtle

def draw_art():
    window = turtle.Screen()
    window.bgcolor("blue")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("orange") # 颜色是橙色
    brad.speed('fast')

    window.exitonclick()

draw_art()