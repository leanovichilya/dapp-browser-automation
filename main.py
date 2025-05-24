from dolphin_anty.fetch import fetch_profiles, extract_reversed_profile_ids
from dolphin_anty.actions import start_profile
from playwright_runner.runner import run_with_ws_endpoint


def main():
    profiles = fetch_profiles()
    profile_ids = extract_reversed_profile_ids(profiles)

    if not profile_ids:
        print("No profiles found.")
        return

    profile_id = profile_ids[0]
    result = start_profile(profile_id)

    if not result or 'automation' not in result:
        print("Failed to start profile.")
        return

    port = result['automation']['port']
    ws_path = result['automation']['wsEndpoint']
    ws_url = f'ws://localhost:{port}{ws_path}'

    print(f"Connecting Playwright to: {ws_url}")
    run_with_ws_endpoint(ws_url)


if __name__ == '__main__':
    main()
