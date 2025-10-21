def draw_rectangle(rows, columns, ch):
    for i in range(rows):
        print(ch * columns)


def draw_right_triangle(rows, ch):
    for i in range(1, rows + 1):
        print(ch * i)


def draw_frame(rows, columns, ch):
    for i in range(rows):
        if i == 0 or i == rows - 1:
            print(ch * columns)
        else:
            print(ch + ' ' * (columns - 2) + ch)

try:
    n = int(input("Введите количество строк: "))
    m = int(input("Введите количество столбцов: "))
    symbol = input("Введите символ для рисования (по умолчанию #): ") or '#'

    print(f"\nВаш прямоугольник {n}x{m}:")
    draw_rectangle(n, m, symbol)

    print(f"\nВаш правый треугольник ({n} строк):")
    draw_right_triangle(n, symbol)

    print(f"\nВаша рамка {n}x{m}:")
    draw_frame(n, m, symbol)

except ValueError:
    print("Ошибка ввода! Используйте целые числа для размеров.")