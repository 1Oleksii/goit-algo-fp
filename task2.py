import turtle
import math

# Функція для малювання лише контуру квадрата
def draw_square(t, p1, p2, p3, p4):
    t.up()
    t.goto(p1)
    t.down()
    t.goto(p2)
    t.goto(p3)
    t.goto(p4)
    t.goto(p1)

# Рекурсивна функція побудови дерева Піфагора
def draw_pythagoras_tree(t, p1, p2, level):
    if level == 0:
        return

    # Обчислюємо вектор сторони квадрата
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]

    # Обчислюємо дві інші точки квадрата (повертаємо вектор на 90 градусів)
    p3 = (p2[0] - dy, p2[1] + dx)
    p4 = (p1[0] - dy, p1[1] + dx)

    # Малюємо квадрат як контур
    draw_square(t, p1, p2, p3, p4)

    # Обчислюємо вершину нового прямокутного трикутника
    px = p4[0] + (dx - dy) / 2
    py = p4[1] + (dy + dx) / 2

    # Рекурсивно малюємо два нових квадрати
    draw_pythagoras_tree(t, p4, (px, py), level - 1)
    draw_pythagoras_tree(t, (px, py), p3, level - 1)

# Основна функція програми
def main():
    try:
        level = int(input("Enter recursion level (1–10): "))
        if level < 1:
            print("Level too low! Setting to 1.")
            level = 1
        elif level > 10:
            print("Level too high! Setting to 10.")
            level = 10
    except ValueError:
        print("Invalid input! Setting recursion level to 5.")
        level = 5

    # Налаштування turtle
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    screen.tracer(False)

    # Початкові координати першого квадрата
    size = 80
    p1 = (-size / 2, -250)
    p2 = (size / 2, -250)

    # Запуск рекурсивної побудови
    draw_pythagoras_tree(t, p1, p2, level)

    screen.tracer(True)
    turtle.done()

if __name__ == "__main__":
    main()
