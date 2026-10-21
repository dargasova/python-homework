def print_menu(prices):
    print("Товары в продаже:")
    for product, price in prices.items():
        print(f"  {product} — {price} руб.")


def ask_quantity(product):
    return int(input(f"Количество «{product}» — целое положительное число (например, 2): "))


def item_cost(price, quantity):
    return price * quantity


def print_receipt(cart):
    print("\n--- Чек ---")
    total = 0
    for number, (product, quantity, cost) in enumerate(cart, start=1):
        print(f"{number}. {product} × {quantity} = {cost} руб.")
        total += cost
    print(f"Сумма: {total} руб.")
    return total


def apply_discount(total, card=False):
    if card:
        discount = int(total * 0.10)
    elif total >= 1000:
        discount = int(total * 0.05)
    else:
        discount = 0
    return discount, total - discount


prices = {"хлеб": 50, "молоко": 90, "сыр": 400, "яблоки": 120, "кофе": 350}
cashier = input("Имя кассира (например, Мария): ")
print(f"Здравствуйте, {cashier}! Касса открыта")
print_menu(prices)

cart = []
while True:
    product = input(
        '\nТовар: хлеб, молоко, сыр, яблоки или кофе (для завершения — "оплата"): '
    ).strip().lower()
    if product == "оплата":
        break
    if product not in prices:
        print(f"Товара «{product}» нет в продаже")
        continue

    quantity = ask_quantity(product)
    cost = item_cost(prices[product], quantity)
    cart.append((product, quantity, cost))
    print(f"Добавлено: {product} × {quantity} = {cost} руб.")

has_card = input("\nКарта магазина — введите только «да» или «нет»: ").strip().lower() == "да"
total = print_receipt(cart)
discount, amount_due = apply_discount(total, card=has_card)
different_products = {product for product, quantity, cost in cart}

print(f"Скидка: {discount} руб.")
print(f"К оплате: {amount_due} руб.")
print(f"Разных товаров в чеке: {len(different_products)}")
print(f"\nСпасибо за работу, {cashier}!")
