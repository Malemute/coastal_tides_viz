from pathlib import Path
from datetime import date

# Корень проекта (файл config.py лежит в src/)
BASE_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = BASE_DIR / "data"
RAW_DIR = DATA_DIR / "raw"
INTERIM_DIR = DATA_DIR / "interim"
PROCESSED_DIR = DATA_DIR / "processed"

MAPS_DIR = BASE_DIR / "maps"
STATIC_MAPS_DIR = MAPS_DIR / "static"
WEB_MAPS_DIR = MAPS_DIR / "web"

# Файлы по умолчанию
AOI_FILE = PROCESSED_DIR / "aoi.geojson"              # область интереса
COASTLINE_FILE = PROCESSED_DIR / "coastline.geojson"  # обрезанная береговая линия
DEM_FILE = RAW_DIR / "dem.tif"                        # DEM по региону (если нужен)
WATER_LEVELS_FILE = INTERIM_DIR / "water_levels.csv"  # уровни воды NOAA

# NOAA / приливы
NOAA_BASE_URL = "https://api.tidesandcurrents.noaa.gov/api/prod/datagetter"
NOAA_DEFAULT_STATION = "8632200"  # пример: поменяешь на свою станцию
NOAA_DEFAULT_PRODUCT = "water_level"
NOAA_DEFAULT_DATUM = "mllw"
NOAA_DEFAULT_TIMEZONE = "gmt"
NOAA_DEFAULT_UNITS = "metric"

# Пример интервала дат для теста
DEFAULT_BEGIN_DATE = date(2024, 1, 1)
DEFAULT_END_DATE = date(2024, 1, 7)