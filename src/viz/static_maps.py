from pathlib import Path
from typing import Dict

import geopandas as gpd
import matplotlib.pyplot as plt

from src.config import STATIC_MAPS_DIR


def plot_inundation_scenarios(
    coastline: gpd.GeoDataFrame,
    scenarios: Dict[str, gpd.GeoDataFrame],
    output_file: Path = STATIC_MAPS_DIR / "inundation_scenarios.png",
) -> None:
    """
    Рисует карту с несколькими сценариями затопления.
    scenarios: словарь {"label": GeoDataFrame}
    """
    STATIC_MAPS_DIR.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(8, 8))

    coastline.plot(ax=ax, alpha=0.5, edgecolor="black")

    for label, gdf in scenarios.items():
        if gdf is None or gdf.empty:
            continue
        gdf.plot(ax=ax, alpha=0.4, label=label)

    ax.set_title("Inundation scenarios")
    ax.legend()
    plt.tight_layout()
    fig.savefig(output_file, dpi=200)
    plt.close(fig)
