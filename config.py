import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv('BASE_URL')
LOCAL_URL = os.getenv('LOCAL_URL')
AUTH_TOKEN = os.getenv('AUTH_TOKEN')

HEADERS = {
    'Authorization': f'Bearer {AUTH_TOKEN}',
    'Content-Type': 'application/json'
}

TARGET_URL = os.getenv('TARGET_URL')
METAMASK_EXTENSION_ID = os.getenv("METAMASK_EXTENSION_ID", "nkbihfbeogaeaoehlefnkodbefgpgknn")
METAMASK_PASSWORD = os.getenv('METAMASK_PASSWORD')

KEEP_OPEN = os.getenv("KEEP_OPEN", "false").lower() == "true"
CLOSE_DELAY_SECONDS = int(os.getenv("CLOSE_DELAY_SECONDS", "5"))