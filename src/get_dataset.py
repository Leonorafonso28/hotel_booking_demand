"""
Download the Hotel Booking Demand dataset (course release v1).

The raw dataset is NOT committed to the repository (per project brief, Dataset
governance section). Run this script once after cloning the repo:

    python src/get_dataset.py

Requires the Kaggle CLI configured with API credentials:
    pip install kaggle
    # then place kaggle.json in ~/.kaggle/ (chmod 600)

Alternative manual download:
    https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand
    place hotel_bookings.csv under  ./data/

After download, this script verifies the MD5 checksum matches the course
release used for the report.
"""

import hashlib
import shutil
import subprocess
import sys
from pathlib import Path

ROOT          = Path(__file__).resolve().parent.parent
DATA_DIR      = ROOT / "data"
DATASET       = DATA_DIR / "hotel_bookings.csv"
EXPECTED_MD5  = "5bf588c5a949443e021fb7c847d31b27"
KAGGLE_SLUG   = "jessemostipak/hotel-booking-demand"


def md5(path: Path) -> str:
    return hashlib.md5(path.read_bytes()).hexdigest()


def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    if DATASET.exists() and md5(DATASET) == EXPECTED_MD5:
        print(f"Dataset already present and checksum matches ({EXPECTED_MD5}).")
        return

    if shutil.which("kaggle") is None:
        sys.exit(
            "Kaggle CLI not found.\n"
            "  pip install kaggle    (then configure ~/.kaggle/kaggle.json)\n"
            "Or download manually from:\n"
            f"  https://www.kaggle.com/datasets/{KAGGLE_SLUG}\n"
            f"and place hotel_bookings.csv in {DATA_DIR}/"
        )

    print(f"Downloading {KAGGLE_SLUG} via Kaggle CLI ...")
    subprocess.run(
        ["kaggle", "datasets", "download", "-d", KAGGLE_SLUG,
         "-p", str(DATA_DIR), "--unzip"],
        check=True,
    )

    if not DATASET.exists():
        sys.exit(f"ERROR: download finished but {DATASET} is not there.")

    got = md5(DATASET)
    if got != EXPECTED_MD5:
        sys.exit(
            f"ERROR: checksum mismatch.\n"
            f"  expected : {EXPECTED_MD5}\n"
            f"  got      : {got}\n"
            f"This is not the course release v1 used in the report."
        )
    print(f"Dataset ready at {DATASET}  (MD5 = {got})")


if __name__ == "__main__":
    main()
