from pathlib import Path
from typing import Optional

import geopandas as gpd

from src.config import COASTLINE_FILE, AOI_FILE


def load_aoi(aoi_file: Path = AOI_FILE) -> gpd.GeoDataFrame:
    """
    Загрузка области интереса (AOI) как GeoDataFrame.
    AOI ты можешь предварительно нарисовать в QGIS и сохранить в GeoJSON.
    """
    if not aoi_file.exists():
        raise FileNotFoundError(f"AOI file not found: {aoi_file}")
    return gpd.read_file(aoi_file)


def load_coastline(coastline_file: Path = COASTLINE_FILE) -> gpd.GeoDataFrame:
    """
    Загрузка предварительно обрезанной береговой линии.
    На первом этапе coastline можно вырезать в QGIS и сохранить в отдельный файл.
    """
    if not coastline_file.exists():
        raise FileNotFoundError(f"Coastline file not found: {coastline_file}")
    return gpd.read_file(coastline_file)


def clip_coastline_to_aoi(
    coastline: gpd.GeoDataFrame,
    aoi: gpd.GeoDataFrame,
) -> gpd.GeoDataFrame:
    """
    Обрезка береговой линии по AOI.
    Эту функцию можно вызывать либо из Python, либо сделать аналог в QGIS.
    """
    coastline = coastline.to_crs(aoi.crs)
    clipped = gpd.overlay(coastline, aoi, how="intersection")
    return clipped
