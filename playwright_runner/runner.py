from .browser import connect_to_browser
from .metamask_handler import handle_metamask
from .page_utils import open_target_page
from .cleanup import cleanup
from dapps.somnia import interact_with_somnia


def run_with_ws_endpoint(ws_endpoint: str):
    playwright, browser, context = connect_to_browser(ws_endpoint)

    # Open dummy page to trigger context
    if not context.pages:
        context.new_page()

    handle_metamask(context)

    page = open_target_page(context)
    interact_with_somnia(page)

    cleanup(playwright, context, browser)
