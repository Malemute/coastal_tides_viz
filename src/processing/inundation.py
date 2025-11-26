from pathlib import Path
from typing import Dict, List

import geopandas as gpd
import numpy as np
import rasterio
from rasterio.features import shapes

from src.config import DEM_FILE


def load_dem(dem_file: Path = DEM_FILE):
    """
    Загрузка DEM через rasterio (каркас).
    """
    if not dem_file.exists():
        raise FileNotFoundError(f"DEM file not found: {dem_file}")
    return rasterio.open(dem_file)


def dem_to_inundation_polygons(
    dem_path: Path,
    water_level_m: float,
    aoi: gpd.GeoDataFrame,
) -> gpd.GeoDataFrame:
    """
    Простейшая модель зоны затопления:
    - читаем DEM
    - создаём маску dem <= water_level_m
    - переводим маску в полигоны
    - обрезаем по AOI

    Это каркас — детали (CRS, nodata, фильтрация мелких полигонов)
    ты допишешь сам.
    """
    with rasterio.open(dem_path) as src:
        dem = src.read(1, masked=True)
        transform = src.transform

        mask = dem <= water_level_m

        shapes_generator = shapes(
            np.where(mask, 1, 0).astype(np.uint8),
            mask=mask,
            transform=transform,
        )

    geoms = []
    values = []

    for geom, value in shapes_generator:
        if value == 1:
            geoms.append(geom)
            values.append(value)

    gdf = gpd.GeoDataFrame({"value": values}, geometry=gpd.GeoSeries.from_geojson(str(geoms)))
    # ↑ здесь придётся поправить конвертацию geom → geometry,
    # я оставляю это как «заглушку»-каркас.

    if not aoi.empty:
        gdf = gdf.set_crs(aoi.crs, allow_override=True)
        gdf = gpd.overlay(gdf, aoi, how="intersection")

    return gdf
