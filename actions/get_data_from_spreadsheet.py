import requests
import sys


def get_data_from_spreadsheet(
    SPREADSHEET_ID: str, SPREADSHEET_TAB: str, GOOGLE_API_KEY: str
) -> dict:
    url = (
        f"https://sheets.googleapis.com/v4/spreadsheets/"
        f"{SPREADSHEET_ID}/values/{SPREADSHEET_TAB}"
        f"?key={GOOGLE_API_KEY}"
    )
    response = requests.get(url)
    if response.status_code != 200:
        print("Помилка запиту:", response.text)
        sys.exit()
    return response.json()
