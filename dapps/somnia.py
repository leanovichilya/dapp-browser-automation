import time
import random
from utils.coin_checker import ensure_strong_coin_on_top
from utils.swap_engine import perform_random_swaps

from playwright.sync_api import TimeoutError


def safe_connect_wallet(page):
    from playwright.sync_api import TimeoutError

    try:
        with page.expect_popup(timeout=5000) as popup_info:
            page.get_by_role("button", name="poweroff Connect").click()
        wallet_popup = popup_info.value

        wallet_popup.get_by_role("button", name="Next").click()
        wallet_popup.get_by_role("button", name="Connect").click()

        print("[Wallet] Подключение подтверждено.")
        return True
    except TimeoutError:
        print("[Wallet] Окно подключения не появилось. Возможно, уже подключено.")
        return False
    except Exception as e:
        print(f"[Wallet] Ошибка при подключении: {e}")
        return False


def interact_with_somnia(page):
    connected = safe_connect_wallet(page)
    if not connected:
        print("[Somnia] Пропускаем подключение — уже подключено или ошибка.")

    page.goto("https://quest.somnia.network/account")

    gsomnia_btn = page.get_by_role("button", name="gSomnia")
    if gsomnia_btn.is_disabled():
        print("[Somnia] gSomnia кнопка отключена. Пропускаем.")
        return

    gsomnia_btn.click()

    time.sleep(2)
    page.get_by_role("button", name="close").click()

    with page.expect_popup() as page1_info:
        page.get_by_role("button", name="Testnet").click()
    page1 = page1_info.value

    perform_random_swaps(page1, iterations=3, min_required_amount=500)

    # page1.goto("https://testnet.somnia.network/")
    # page1.get_by_role("button", name="Request Tokens").click()
    # page1.get_by_role("button", name="Get STT").click()
    # page1.get_by_role("button", name="Send Tokens").click()
    # page1.get_by_role("button", name="0.001 STT").click()
    # page1.get_by_role("button", name="0.005 STT").click()
    # page1.get_by_role("button", name="0.01 STT").click()
    # page1.get_by_role("button", name="0.001 STT").click()
    # page1.get_by_role("button", name="Random Address").click()
    # page1.get_by_role("button", name="Send STT").click()
    #
    # page2_promise = page1.wait_for_event("popup")
    # page1.get_by_role("button", name="Go Quest").click()
    # page2 = page2_promise.value
    # page2.close()
