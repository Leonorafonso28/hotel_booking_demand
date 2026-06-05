"""
Single-entry point for the Hotel Booking Demand clustering pipeline.

Usage:
    python run_all.py

- Verifies dataset presence and MD5 checksum (raw data is NOT in the repo).
- Wipes experiments.csv and figures/, tables/ at the start so every run is clean.
- Executes all notebooks in the correct order, end-to-end, with no manual steps.
"""

import hashlib
import shutil
import subprocess
import sys
from pathlib import Path

ROOT       = Path(__file__).resolve().parent
DATA_DIR   = ROOT / "data"
NB_DIR     = ROOT / "notebooks"
FIG_DIR    = ROOT / "figures"
TBL_DIR    = ROOT / "tables"
EXP_CSV    = ROOT / "experiments.csv"

DATASET      = DATA_DIR / "hotel_bookings.csv"
EXPECTED_MD5 = "8388523d9b568014188662c5721dee2b"   # course release v1

NOTEBOOKS = [
    "ANS_Task1.ipynb",      # EDA, R0 representation, k-means + iK-means
    "ANS_Task2.ipynb",      # Ward hierarchical, stability
    "ANS_Task3.ipynb",      # internal indices, sensitivity, cross-method ARI
    "ANS_Module1.ipynb",    # Extension E1 - cluster-aware anomalies
    "ANS_Module3.ipynb",    # Extension E3 - fuzzy c-means
    "ANS_Module4.ipynb",    # Extension E4 - PCA dimensionality reduction
]

def check_dataset() -> None:
    """Fail fast if the raw dataset is missing or has the wrong checksum."""
    if not DATASET.exists():
        sys.exit(
            f"\nERROR: dataset not found at {DATASET}\n"
            f"   Download it with:  python src/get_dataset.py\n"
            f"   (see README.md for details)\n"
        )
    md5 = hashlib.md5(DATASET.read_bytes()).hexdigest()
    if md5 != EXPECTED_MD5:
        sys.exit(
            f"\nERROR: dataset checksum mismatch.\n"
            f"   expected : {EXPECTED_MD5}\n"
            f"   found    : {md5}\n"
            f"   You may have a different release of the file.\n"
        )
    print(f"  Dataset OK  ({DATASET.name}, MD5 = {md5})")


def clean_outputs() -> None:
    """Remove previous run artefacts so the pipeline is reproducible from scratch."""
    for d in (FIG_DIR, TBL_DIR):
        if d.exists():
            shutil.rmtree(d)
        d.mkdir(parents=True, exist_ok=True)
    if EXP_CSV.exists():
        EXP_CSV.unlink()
    print("  Cleaned figures/, tables/, experiments.csv")


def execute_notebook(nb_name: str) -> None:
    """Execute a notebook in place. Halt the pipeline on the first failure."""
    nb_path = NB_DIR / nb_name
    if not nb_path.exists():
        sys.exit(f"ERROR: notebook not found: {nb_path}")

    print(f"\n-> Running {nb_name} ...")
    try:
        subprocess.run(
            ["jupyter", "nbconvert", "--to", "notebook",
             "--execute", "--inplace", str(nb_path)],
            check=True,
        )
        print(f"   done: {nb_name}")
    except subprocess.CalledProcessError:
        sys.exit(f"ERROR executing {nb_name}. Pipeline halted.")


def main() -> None:
    print("=== Hotel Booking Clustering Pipeline ===\n")

    check_dataset()
    clean_outputs()

    for nb in NOTEBOOKS:
        execute_notebook(nb)

    print("\n=== Pipeline finished ===")
    print(f"  figures/        : {FIG_DIR}")
    print(f"  tables/         : {TBL_DIR}")
    print(f"  experiments.csv : {EXP_CSV}")


if __name__ == "__main__":
    main()