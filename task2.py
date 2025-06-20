import turtle
import math

def draw_pythagoras_tree(t, branch_length, level):
    if level == 0:
        return

    # Малюємо основну гілку
    t.forward(branch_length)

    # Зберігаємо поточну позицію та напрямок
    pos = t.pos()
    angle = t.heading()

    # Обчислюємо довжину наступних гілок
    new_length = branch_length * math.cos(math.radians(45))

    # Ліва гілка
    t.left(45)
    draw_pythagoras_tree(t, new_length, level - 1)

    # Повертаємось
    t.penup()
    t.setpos(pos)
    t.setheading(angle)
    t.pendown()

    # Права гілка
    t.right(45)
    draw_pythagoras_tree(t, new_length, level - 1)

    # Повертаємось
    t.penup()
    t.setpos(pos)
    t.setheading(angle)
    t.pendown()

def main():
    level = int(input("Введіть рівень рекурсії (рекомендується 5–12): "))

    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.color("brown")
    t.left(90)  # Направлення вгору
    t.penup()
    t.goto(0, -250)
    t.pendown()

    draw_pythagoras_tree(t, 100, level)

    screen.mainloop()

if __name__ == "__main__":
    main()
