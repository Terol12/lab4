
while True:
    packets = input("Введите последовательность из 0 и 1: ")

    if len(packets) < 5:
        print("Ошибка: минимальная длина - 5 символов!")
        continue

    if not all(char in '01' for char in packets):
        print("Ошибка: используйте только '0' и '1'!")
        continue

    break

total = len(packets)
lost = packets.count('0')

max_zero = 0
current = 0
for char in packets:
    if char == '0':
        current += 1
        if current > max_zero:
            max_zero = current
    else:
        current = 0

percent = (lost / total) * 100

if percent <= 1:
    quality = "Отличное качество"
elif percent <= 5:
    quality = "Хорошее качество"
elif percent <= 10:
    quality = "Удовлетворительное качество"
elif percent <= 20:
    quality = "Плохое качество"
else:
    quality = "Критическое состояние сети"

print(f"\nОбщее количество пакетов: {total}")
print(f"Количество потерянных пакетов: {lost}")
print(f"Длина самой длинной последовательности потерянных пакетов: {max_zero}")
print(f"Процент потерь: {percent:.1f}%")
print(f"Качество связи: {quality}")
