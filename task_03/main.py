last_name = input("Ваша фамилия (например, Кузнецова): ")
first_name = input("Ваше имя (например, Ольга): ")
print(f"Добро пожаловать, {first_name}! Начинаем приём заявок")

total_applicants = 0
accepted_applicants = 0

while True:
    applicant = input(
        '\nФамилия абитуриента, например Петров (или "завершить"): '
    ).strip()
    if applicant.lower() == "завершить":
        break

    score = int(input("Балл абитуриента (целое число, например 235): "))
    has_diploma = input("Диплом олимпиады — введите только «да» или «нет»: ").strip().lower()
    is_accepted = score >= 220 or (has_diploma == "да" and score >= 180)

    total_applicants += 1
    if is_accepted:
        accepted_applicants += 1
        print(f"{applicant}: заявка одобрена")
    else:
        print(f"{applicant}: заявка отклонена")

print(f"\nРассмотрено абитуриентов: {total_applicants}")
print(f"Зачислено: {accepted_applicants}")
print(f"\nДо свидания, {first_name}!")
