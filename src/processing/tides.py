from typing import List

import pandas as pd


def select_characteristic_times(
    df: pd.DataFrame,
    n_high: int = 2,
    n_low: int = 2,
) -> pd.DataFrame:
    """
    Выбор нескольких характерных моментов:
    - n_high максимумов
    - n_low минимумов

    Предполагаем, что в df есть колонки:
    - datetime
    - water_level
    """
    if df.empty:
        return df

    df_sorted = df.sort_values("datetime")

    # Простая версия: берём top-n по уровню и bottom-n.
    highs = df_sorted.nlargest(n_high, "water_level")
    lows = df_sorted.nsmallest(n_low, "water_level")

    result = pd.concat([highs, lows]).drop_duplicates().sort_values("datetime")
    return result
