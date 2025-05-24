from config import METAMASK_PASSWORD


def unlock_metamask(page):
    try:
        page.wait_for_selector('input[type="password"]', timeout=5000)
        page.fill('input[type="password"]', METAMASK_PASSWORD)
        page.click('button:has-text("Unlock")')
        print("[Metamask] Unlocked successfully.")
    except Exception as e:
        print(f"[Metamask] Unlock failed: {e}")
