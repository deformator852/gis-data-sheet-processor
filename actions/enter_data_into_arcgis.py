import pandas as pd
from arcgis.gis import GIS


def enter_data_into_arcgis(
    df: pd.DataFrame,
    ARCGIS_USERNAME: str,
    ARCGIS_PASSWORD: str,
    ARCGIS_HOSTED_FEATURE_LAYER: str,
):
    gis = GIS("https://www.arcgis.com", ARCGIS_USERNAME, ARCGIS_PASSWORD)
    item = gis.content.get(ARCGIS_HOSTED_FEATURE_LAYER)

    feature_layer = item.layers[0]
    features = []

    for _, row in df.iterrows():
        feature = {
            "geometry": {
                "x": float(str(row["long"]).replace(",", ".")),
                "y": float(str(row["lat"]).replace(",", ".")),
                "spatialReference": {"wkid": 4326},
            },
            "attributes": {
                "date_1": row["Дата"],
                "Область": row["Область"],
                "city": row["Місто"],
                "value_1": row["Значення 1"],
                "value_2": row["Значення 2"],
                "value_3": row["Значення 3"],
                "value_4": row["Значення 4"],
                "value_5": row["Значення 5"],
                "value_6": row["Значення 6"],
                "value_7": row["Значення 7"],
                "value_8": row["Значення 8"],
                "value_9": row["Значення 9"],
                "value_10": row["Значення 10"],
                "long": float(str(row["long"]).replace(",", ".")),
                "lat": float(str(row["lat"]).replace(",", ".")),
            },
        }

        features.append(feature)

    feature_layer.edit_features(adds=features)
