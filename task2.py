import turtle
import math

# Функція рекурсивного малювання дерева Піфагора
def draw_pythagoras_tree(t, length, level):
    if level == 0:
        return

    # Малюємо вертикальний відрізок
    t.forward(length)
    t.left(90)

    # Зберігаємо координати та напрям черепахи
    x, y = t.pos()
    angle = t.heading()

    # Обчислюємо довжину нових гілок (за теоремою Піфагора)
    new_length = length * math.sqrt(2) / 2

    # Малюємо ліву гілку
    t.left(45)
    draw_pythagoras_tree(t, new_length, level - 1)

    # Повертаємося назад до вузла
    t.setpos(x, y)
    t.setheading(angle)

    # Малюємо праву гілку
    t.right(45)
    draw_pythagoras_tree(t, new_length, level - 1)

    # Повертаємося назад і відступаємо назад
    t.setpos(x, y)
    t.setheading(angle)
    t.backward(length)

# Основна функція
def main():
    # Запит рівня рекурсії з перевіркою вводу
    try:
        level = int(input("Enter recursion level (1-10): "))
        if level < 1:
            print("Level too low! Setting to 1.")
            level = 1
        elif level > 10:
            print("Level too high! Setting to 10.")
            level = 10
    except ValueError:
        print("Invalid input! Setting recursion level to 5.")
        level = 5

    # Налаштування вікна turtle
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.hideturtle()            # Ховаємо курсор
    t.speed(0)                # Найшвидша швидкість
    screen.tracer(False)      # Вимикаємо анімацію для пришвидшення

    # Встановлюємо початкову позицію внизу по центру
    t.penup()
    t.goto(0, -250)
    t.setheading(90)          # Напрям вгору
    t.pendown()

    # Запускаємо рекурсивне малювання дерева
    draw_pythagoras_tree(t, 80, level)

    screen.tracer(True)       # Вмикаємо анімацію після малювання
    turtle.done()             # Завершення програми

# Точка входу
if __name__ == "__main__":
    main()
