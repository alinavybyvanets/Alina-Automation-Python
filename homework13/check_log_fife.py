import os
from log_event_module import log_event

LOG_FILE = "login_system.log"

log_event("alina", "success")

if os.path.exists(LOG_FILE):
    print(f"✅ Файл {LOG_FILE} створено успішно!")
else:
    print(f"❌ Файл {LOG_FILE} не знайдено.")