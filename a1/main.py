import random
import time


while True:
    try:
        N = int(input("Введите количество примеров: "))
        if N > 0:
            break
        else:
            print("Количество примеров должно быть положительным числом!")
    except ValueError:
        print("Пожалуйста, введите целое число!")

correct_answers = 0
total_time = 0
question_times = []

print()

for i in range(1, N + 1):
    print(f"Вопрос {i}/{N}")

    a = random.randint(2, 9)
    b = random.randint(2, 9)
    correct_result = a * b

    while True:
        try:
            start_time = time.time()
            user_answer = input(f"{a} × {b} = ")
            end_time = time.time()

            time_spent = end_time - start_time
            user_answer = int(user_answer)
            break

        except ValueError:
            print("Пожалуйста, введите целое число!")

    if user_answer == correct_result:
        print(f"Верно! (Время: {time_spent:.1f} сек)")
        correct_answers += 1
    else:
        print(f"Неверно! Правильно: {correct_result} (Время: {time_spent:.1f} сек)")

    total_time += time_spent
    question_times.append(time_spent)

    print()

print("=" * 50)
print("СТАТИСТИКА:")
print("=" * 50)
print(f"Общее время: {total_time:.1f} секунд")
print(f"Среднее время на вопрос: {total_time / N:.1f} сек")
print(f"Правильных ответов: {correct_answers}/{N}")
print(f"Процент правильных: {correct_answers / N * 100:.1f}%")

