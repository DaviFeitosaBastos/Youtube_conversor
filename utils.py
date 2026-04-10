import sys
from pathlib import Path


def get_base_dir():
    if hasattr(sys, '_MEIPASS'):
        return Path(sys.executable).parent
    return Path(__file__).parent