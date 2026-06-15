import logging
import os
from datetime import datetime

# Create timestamp only once when framework starts
RUN_TIMESTAMP = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def get_logger(name="automation"):

    logger = logging.getLogger(name)

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    # Create logs directory
    os.makedirs("logs", exist_ok=True)

    # Get pytest-xdist worker id
    worker_id = os.getenv("PYTEST_XDIST_WORKER", "master")

    # Log file name
    log_file = f"logs/test_run_{worker_id}_{RUN_TIMESTAMP}.log"

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-5s | %(filename)s:%(lineno)d | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # File Handler
    file_handler = logging.FileHandler(
        log_file,
        mode="a",
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


