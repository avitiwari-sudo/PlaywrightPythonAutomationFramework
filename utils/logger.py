import logging
import os
from datetime import datetime


def get_logger(name="automation"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Avoid duplicate handlers
    if not logger.handlers:
        # Create logs directory if not exists
        os.makedirs("logs", exist_ok=True)
        # Worker ID from pytest-xdist
        worker_id = os.getenv("PYTEST_XDIST_WORKER", "worker0")

        # Timestamp for unique log file
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        log_file = f"logs/test_{worker_id}_{timestamp}.log"

        file_handler = logging.FileHandler(log_file)
        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)-5s | %(filename)s:%(lineno)d | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )
        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger