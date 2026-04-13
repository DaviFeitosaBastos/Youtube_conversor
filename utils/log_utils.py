import sys
import logging
from rich.logging import RichHandler
from pathlib import Path



def get_base_dir():
    if hasattr(sys, '_MEIPASS'):
        return Path(sys.executable).parent
    return Path(__file__).parent


def get_logger(name: str) -> logging.Logger:
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] %(levelname)s | %(name)s | %(message)s",
        handlers=[
            RichHandler(rich_tracebacks=True),
            logging.FileHandler(get_base_dir() / "app.log")
        ]
    )
    return logging.getLogger(name)