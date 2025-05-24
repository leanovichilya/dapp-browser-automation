import requests
from config import LOCAL_URL


def start_profile(profile_id):
    """Starts a browser profile by its ID."""
    try:
        url = f'{LOCAL_URL}/browser_profiles/{profile_id}/start?automation=1'
        response = requests.get(url)
        response.raise_for_status()
        print(f'Profile {profile_id} started successfully.')
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f'Failed to start profile {profile_id}: {e}')
        return None
