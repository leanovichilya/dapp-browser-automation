import random
from utils.coin_checker import ensure_strong_coin_on_top


def perform_random_swaps(page, iterations=3, min_required_amount=1000):
    """Переводит случайные суммы между монетами заданное количество раз."""

    for i in range(iterations):
        print(f"[SwapEngine] Swap iteration {i+1}/{iterations}")

        # Убедиться, что сверху достаточная монета
        coin_name, coin_amount = ensure_strong_coin_on_top(page, min_amount=min_required_amount)

        # Случайное значение в пределах монеты
        amount = round(random.uniform(0.1, 0.8) * coin_amount, 4)

        # Ввод значения
        input_field = page.locator('input[name="amountIn"]')
        input_field.click()
        input_field.fill(str(amount))

        # Случайная перестановка монет
        if random.choice([True, False]):
            print("[SwapEngine] Flipping coin direction")
            page.get_by_role("img", name="swap").click()

        # Нажимаем "Swap"
        print(f"[SwapEngine] Swapping {amount} {coin_name}")
        page.get_by_role("button", name="Swap", exact=True).click()

        # Небольшая пауза
        page.wait_for_timeout(2000)
