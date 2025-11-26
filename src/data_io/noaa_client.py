import datetime as dt
from typing import Optional

import pandas as pd
import requests

from src.config import (
    NOAA_BASE_URL,
    NOAA_DEFAULT_STATION,
    NOAA_DEFAULT_PRODUCT,
    NOAA_DEFAULT_DATUM,
    NOAA_DEFAULT_TIMEZONE,
    NOAA_DEFAULT_UNITS,
    WATER_LEVELS_FILE,
)


def fetch_water_levels(
    station_id: str = NOAA_DEFAULT_STATION,
    begin_date: dt.date = None,
    end_date: dt.date = None,
    product: str = NOAA_DEFAULT_PRODUCT,
    datum: str = NOAA_DEFAULT_DATUM,
    time_zone: str = NOAA_DEFAULT_TIMEZONE,
    units: str = NOAA_DEFAULT_UNITS,
    save_to_csv: bool = True,
) -> pd.DataFrame:
    """
    Запрос уровней воды с NOAA Tides & Currents API.

    Пока без обработки ошибок и пагинации — минимальный каркас.
    """
    if begin_date is None or end_date is None:
        raise ValueError("begin_date и end_date должны быть заданы явно")

    params = {
        "product": product,
        "application": "coastal_tides_viz",
        "begin_date": begin_date.strftime("%Y%m%d"),
        "end_date": end_date.strftime("%Y%m%d"),
        "datum": datum,
        "station": station_id,
        "time_zone": time_zone,
        "units": units,
        "format": "json",
    }

    response = requests.get(NOAA_BASE_URL, params=params)
    response.raise_for_status()

    data = response.json()

    # Здесь предполагаем, что в ответе есть ключ "data"
    # Ты допишешь обработку под фактическую структуру.
    records = data.get("data", [])
    df = pd.DataFrame.from_records(records)

    # Приводим время и уровни к удобному виду
    if not df.empty:
        if "t" in df.columns:
            df["datetime"] = pd.to_datetime(df["t"])
        if "v" in df.columns:
            df["water_level"] = pd.to_numeric(df["v"], errors="coerce")

    if save_to_csv:
        WATER_LEVELS_FILE.parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(WATER_LEVELS_FILE, index=False)

    return df
