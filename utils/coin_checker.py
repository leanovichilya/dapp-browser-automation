def get_coin_info(page, index: int):
    """Извлекает имя и количество монеты из формы обмена"""
    container = page.locator('div.flex.justify-between.items-center').nth(index)
    name = container.locator('span.text-base').text_content()
    amount = container.locator('xpath=../../../div[contains(@class, "flex.justify-end")]//span').text_content()
    return name.strip(), float(amount.strip())


def ensure_strong_coin_on_top(page, min_amount: float = 500):
    """Проверяет верхнюю монету и делает swap, если баланс ниже минимального"""
    name, amount = get_coin_info(page, 0)
    if amount < min_amount:
        print(f"[CoinChecker] {name} слишком мало ({amount}), выполняем swap...")
        page.get_by_role("img", name="swap").click()
        page.wait_for_timeout(500)
        name, amount = get_coin_info(page, 0)
        print(f"[CoinChecker] После swap: {name} ({amount})")
    else:
        print(f"[CoinChecker] Монета {name} достаточна ({amount})")

    return name, float(amount)
