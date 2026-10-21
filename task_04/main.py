coach_surname = input("Ваша фамилия (например, Смирнов): ")
coach_name = input("Ваше имя (например, Андрей): ")
print(f"Добро пожаловать, {coach_name}! Начинаем принимать зачёт")

athletes_count = int(input("\nКоличество спортсменов — целое положительное число (например, 3): "))
attempts_count = int(input("Количество подходов — целое положительное число (например, 3): "))

surnames = []
totals = []
passed_count = 0

for athlete_number in range(1, athletes_count + 1):
    print(f"\n--- Спортсмен {athlete_number} ---")
    surname = input("Фамилия спортсмена (например, Петров): ")
    athlete_total = 0

    for attempt_number in range(1, attempts_count + 1):
        athlete_total += int(
            input(
                f"Подход {attempt_number} — целое неотрицательное число подтягиваний (например, 10): "
            )
        )

    surnames.append(surname)
    totals.append(athlete_total)

    if athlete_total >= 30:
        passed_count += 1
        result = "норматив выполнен"
    else:
        result = "норматив не выполнен"
    print(f"{surname}: всего {athlete_total} — {result}")

print("\nИтоговая таблица:")
for index in range(len(surnames)):
    print(f"{index + 1}. {surnames[index]} — {totals[index]}")

print(f"\nНорматив выполнили: {passed_count} из {athletes_count}")
print(f"Всего подтягиваний группы: {sum(totals)}")
print(f"\nДо свидания, {coach_name}!")
