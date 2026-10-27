import os


def load_catalog(filename):
    catalog = {}

    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()
                if not line:
                    continue

                fields = line.split(";")
                if len(fields) != 4:
                    print(f"Строка {line_number} пропущена: ожидается 4 поля.")
                    continue

                book_id_text, title, price_text, quantity_text = fields
                try:
                    book_id = int(book_id_text)
                    price = int(price_text)
                    quantity = int(quantity_text)
                except ValueError:
                    print(f"Строка {line_number} пропущена: ID, цена и количество должны быть целыми числами.")
                    continue

                title = title.strip()
                if book_id < 1 or price <= 0 or quantity < 0 or not title:
                    print(f"Строка {line_number} пропущена: недопустимые данные книги.")
                    continue
                if book_id in catalog:
                    print(f"Строка {line_number} пропущена: ID {book_id} уже используется.")
                    continue

                catalog[book_id] = (title, price, quantity)
    except FileNotFoundError:
        print(f"Файл «{filename}» не найден. Создан пустой каталог.")
        return {}

    print(f"Файл catalog.txt загружен. Книг в каталоге: {len(catalog)}")
    return catalog


def save_catalog(filename, catalog):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            for book_id in sorted(catalog):
                title, price, quantity = catalog[book_id]
                file.write(f"{book_id};{title};{price};{quantity}\n")
    except OSError as error:
        print(f"Не удалось сохранить каталог: {error}")
        return False

    print("Каталог сохранён в файл catalog.txt.")
    return True


def print_catalog(catalog):
    if not catalog:
        print("Каталог пуст.")
        return

    print("\nКаталог:")
    for book_id in sorted(catalog):
        title, price, quantity = catalog[book_id]
        availability = f"остаток: {quantity}" if quantity > 0 else "нет в наличии"
        print(f"{book_id}. {title} — {price} руб., {availability}")


def add_book(catalog):
    try:
        book_id = int(input("ID новой книги — целое число от 1 (например, 6): "))
    except ValueError:
        print("ID должен быть целым числом.")
        return False

    if book_id < 1:
        print("ID должен быть не меньше 1.")
        return False
    if book_id in catalog:
        print(f"Книга с ID {book_id} уже есть в каталоге.")
        return False

    title = input("Название книги — непустой текст без точки с запятой: ").strip()
    if not title or ";" in title:
        print("Название не должно быть пустым или содержать точку с запятой.")
        return False

    try:
        price = int(input("Цена в рублях — целое число больше 0 (например, 590): "))
    except ValueError:
        print("Цена должна быть целым числом.")
        return False

    try:
        quantity = int(input("Количество — целое число от 0 (например, 3): "))
    except ValueError:
        print("Количество должно быть целым числом.")
        return False

    if price <= 0:
        print("Цена должна быть больше 0.")
        return False
    if quantity < 0:
        print("Количество не может быть отрицательным.")
        return False

    catalog[book_id] = (title, price, quantity)
    print(f"Книга «{title}» добавлена.")
    return True


def delete_book(catalog):
    try:
        book_id = int(input("ID удаляемой книги — целое число (например, 5): "))
    except ValueError:
        print("ID должен быть целым числом.")
        return False

    if book_id not in catalog:
        print(f"Книги с ID {book_id} нет в каталоге.")
        return False

    title = catalog[book_id][0]
    del catalog[book_id]
    print(f"Книга «{title}» удалена.")
    return True


def change_price(catalog):
    try:
        book_id = int(input("ID книги для изменения цены — целое число: "))
    except ValueError:
        print("ID должен быть целым числом.")
        return False

    if book_id not in catalog:
        print(f"Книги с ID {book_id} нет в каталоге.")
        return False

    try:
        new_price = int(input("Новая цена — целое число больше 0 (например, 560): "))
    except ValueError:
        print("Цена должна быть целым числом.")
        return False

    if new_price <= 0:
        print("Цена должна быть больше 0.")
        return False

    title, old_price, quantity = catalog[book_id]
    catalog[book_id] = (title, new_price, quantity)
    print(f"Цена книги «{title}» изменена с {old_price} на {new_price} руб.")
    return True


def change_quantity(catalog):
    try:
        book_id = int(input("ID книги для изменения количества — целое число: "))
    except ValueError:
        print("ID должен быть целым числом.")
        return False

    if book_id not in catalog:
        print(f"Книги с ID {book_id} нет в каталоге.")
        return False

    try:
        new_quantity = int(input("Новое количество — целое число от 0 (например, 4): "))
    except ValueError:
        print("Количество должно быть целым числом.")
        return False

    if new_quantity < 0:
        print("Количество не может быть отрицательным.")
        return False

    title, price, old_quantity = catalog[book_id]
    catalog[book_id] = (title, price, new_quantity)
    print(f"Количество книги «{title}» изменено с {old_quantity} на {new_quantity}.")
    return True


def run_store(filename):
    catalog = load_catalog(filename)

    while True:
        print(
            "\nМеню:\n"
            "1 — показать каталог\n"
            "2 — добавить книгу\n"
            "3 — удалить книгу\n"
            "4 — изменить цену\n"
            "5 — изменить количество\n"
            "0 — сохранить и выйти"
        )

        try:
            choice = int(input("Выберите пункт — целое число от 0 до 5: "))
        except ValueError:
            print("Пункт меню должен быть целым числом от 0 до 5.")
            continue

        if choice == 1:
            print_catalog(catalog)
        elif choice == 2:
            add_book(catalog)
        elif choice == 3:
            delete_book(catalog)
        elif choice == 4:
            change_price(catalog)
        elif choice == 5:
            change_quantity(catalog)
        elif choice == 0:
            save_catalog(filename, catalog)
            print("До свидания!")
            break
        else:
            print("Такого пункта нет. Выберите число от 0 до 5.")


def catalog_filename():
    return os.path.join(os.path.dirname(__file__), "catalog.txt")


if __name__ == "__main__":
    run_store(catalog_filename())
