import requests
from config import BASE_URL, HEADERS


def fetch_profiles():
    """Fetches all profiles from Dolphin Anty API."""
    try:
        response = requests.get(f'{BASE_URL}/browser_profiles', headers=HEADERS)
        response.raise_for_status()
        return response.json().get('data', [])
    except requests.exceptions.RequestException as e:
        print(f'API request error: {e}')
        return []


def extract_reversed_profile_ids(profiles):
    """Extracts and reverses profile IDs from the list of profiles."""
    return list(reversed([profile.get('id') for profile in profiles]))
