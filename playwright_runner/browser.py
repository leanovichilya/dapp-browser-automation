from playwright.sync_api import sync_playwright


def connect_to_browser(ws_endpoint):
    playwright = sync_playwright().start()
    browser = playwright.chromium.connect_over_cdp(ws_endpoint)
    context = browser.contexts[0]
    return playwright, browser, context
