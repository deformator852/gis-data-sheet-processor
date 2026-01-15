def generate_rows_for_nonzero_values(row) -> list:
    """
    Створює нові рядки для всіх колонок Значення 1–10 з ненульовими значеннями.
    Повертає список словників для нових рядків.
    """
    new_rows = [{}, {}, {}]
    for new_row in new_rows:
        for col in ["Дата", "Область", "Місто", "lat", "long"]:
            new_row[col] = str(row[col])
        for i in range(1, 11):
            if int(row[f"Значення {i}"]) >= 1:
                new_row[f"Значення {i}"] = "1"
                continue

            new_row[f"Значення {i}"] = "0"
    return new_rows
