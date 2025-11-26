import datetime as dt

from src.config import (
    DEFAULT_BEGIN_DATE,
    DEFAULT_END_DATE,
    NOAA_DEFAULT_STATION,
)
from src.data_io.noaa_client import fetch_water_levels
from src.processing.tides import select_characteristic_times


def main():
    print("=== Coastal Tides Viz ===")

    # 1. Получаем уровни воды
    print("Fetching water levels from NOAA...")
    df = fetch_water_levels(
        station_id=NOAA_DEFAULT_STATION,
        begin_date=DEFAULT_BEGIN_DATE,
        end_date=DEFAULT_END_DATE,
    )

    if df.empty:
        print("No data received from NOAA.")
        return

    print(f"Received {len(df)} records.")

    # 2. Выбираем характерные моменты (максимумы/минимумы)
    characteristic = select_characteristic_times(df, n_high=2, n_low=2)
    print("Characteristic times:")
    print(characteristic[["datetime", "water_level"]])

    # 3. Здесь позже:
    #    - построить полигоны затопления для выбранных уровней
    #    - визуализировать сценарии статически или интерактивно


if __name__ == "__main__":
    main()
