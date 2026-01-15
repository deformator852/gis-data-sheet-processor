import os
import sys


def get_env() -> list:
    required_vars = [
        "SPREADSHEET_ID",
        "SPREADSHEET_TAB",
        "GOOGLE_API_KEY",
        "ARCGIS_USERNAME",
        "ARCGIS_PASSWORD",
        "ARCGIS_HOSTED_FEATURE_LAYER",
    ]

    env_values = []

    for var in required_vars:
        value = os.environ.get(var)
        if not value:
            print(f"Відсутній {var} в .env")
            sys.exit()
        env_values.append(value)

    return env_values
