from config import METAMASK_EXTENSION_ID
from .metamask import unlock_metamask


def open_metamask_extension(context):
    metamask_url = f"chrome-extension://{METAMASK_EXTENSION_ID}/home.html"
    metamask_page = context.new_page()
    metamask_page.goto(metamask_url)
    return metamask_page


def handle_metamask(context):
    print("[Runner] Opening MetaMask...")
    metamask_page = open_metamask_extension(context)

    print("[Runner] Unlocking MetaMask...")
    unlock_metamask(metamask_page)

    metamask_page.close()
    print("[Runner] MetaMask tab closed.")
