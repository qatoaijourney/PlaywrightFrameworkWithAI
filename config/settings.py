import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
TESTDATA_DIR = BASE_DIR / "testdata"
REPORTS_DIR = BASE_DIR / "reports"

BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com")
DEFAULT_TIMEOUT = 10_000
