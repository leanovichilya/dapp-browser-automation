import time
from config import KEEP_OPEN, CLOSE_DELAY_SECONDS


def cleanup(playwright, context, browser):
    if not KEEP_OPEN:
        print(f"[Runner] Waiting {CLOSE_DELAY_SECONDS} seconds before closing browser...")
        time.sleep(CLOSE_DELAY_SECONDS)

        for page in context.pages:
            try:
                page.close()
            except Exception as e:
                print(f"[Runner] Failed to close page: {e}")

        try:
            context.close()
            browser.close()
            print("[Runner] Browser closed.")
        except Exception as e:
            print(f"[Runner] Failed to close browser: {e}")
        finally:
            playwright.stop()
    else:
        print("[Runner] KEEP_OPEN is true. Browser will remain open.")
