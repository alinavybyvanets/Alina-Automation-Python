
import logging
LOG_FILE = "login_system.log"

# Створення та налаштування логера
logger = logging.getLogger("log_event")
logger.setLevel(logging.INFO)
if not logger.handlers:
    file_handler = logging.FileHandler(LOG_FILE)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

def log_event(username: str, status: str):
    log_message = f"Login event - Username: {username}, Status: {status}"


    # Логування події
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)
