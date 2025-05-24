from config import TARGET_URL


def open_target_page(context):
    print("[Runner] Opening target DApp page...")
    page = context.new_page()
    page.goto(TARGET_URL, wait_until="domcontentloaded")
    print("[Runner] Automation ready.")
    return page
