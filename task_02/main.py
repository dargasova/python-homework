full_name = input(
    "Введите фамилию, имя и отчество через пробел (например, Иванов Иван Иванович): "
).split()
surname, name, patronymic = full_name

print(f"Здравствуйте, {name}!")

shopping_list = [
    input("Первый товар — одно название (например, яблоки): "),
    input("Второй товар — одно название (например, хлеб): "),
    input("Третий товар — одно название (например, молоко): "),
]

print(f"Ваш список: {shopping_list}")
print(f"Товаров в списке: {len(shopping_list)}")

shopping_list.append("стакан")
print(f"Список после добавления подарка: {shopping_list}")

shopping_list.sort()
print(f"Отсортированный список: {shopping_list}")
print(f"До свидания, {name[0]}.{patronymic[0]}. {surname}!")
