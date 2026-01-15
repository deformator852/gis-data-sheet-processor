import sys
import pandas as pd
from dotenv import load_dotenv
from actions.enter_data_into_arcgis import enter_data_into_arcgis
from actions.generate_rows_for_5_3 import generate_rows_for_5_3
from actions.generate_rows_for_nonzero_values import generate_rows_for_nonzero_values
from actions.get_data_from_spreadsheet import get_data_from_spreadsheet
from actions.get_env import get_env

load_dotenv()


def main():
    [
        SPREADSHEET_ID,
        SPREADSHEET_TAB,
        GOOGLE_API_KEY,
        ARCGIS_USERNAME,
        ARCGIS_PASSWORD,
        ARCGIS_HOSTED_FEATURE_LAYER,
    ] = get_env()
    print("📥 Отримання даних з Google Sheets")
    data_json = get_data_from_spreadsheet(
        SPREADSHEET_ID, SPREADSHEET_TAB, GOOGLE_API_KEY
    )
    print("✅ Дані отримано")
    values = data_json.get("values", [])
    new_data_df = pd.DataFrame()
    new_rows_list = []
    data_df = pd.DataFrame(values[1:], columns=values[0])
    print("⚙️ Обробка даних")
    for _, row in data_df.iterrows():
        if row["Значення 1"] == "5" and row["Значення 2"] == "3":
            new_rows_list.extend(generate_rows_for_5_3(row))
            continue
        nonzero_values = {
            i: row[f"Значення {i}"]
            for i in range(1, 11)
            if row[f"Значення {i}"] != "0" and row[f"Значення {i}"] != 0
        }
        if not nonzero_values:
            continue
        new_rows_list.extend(generate_rows_for_nonzero_values(row))

    if new_rows_list:
        new_data_df = pd.DataFrame(new_rows_list)
    else:
        print("Відсутні нові рядки")
        sys.exit()
    print("✅ Дані оброблено")
    print("🗺️  Занесення даних в ArcGIS")
    enter_data_into_arcgis(
        new_data_df, ARCGIS_USERNAME, ARCGIS_PASSWORD, ARCGIS_HOSTED_FEATURE_LAYER
    )
    print("✅ Дані в Arcgis занесено")


if __name__ == "__main__":
    main()
