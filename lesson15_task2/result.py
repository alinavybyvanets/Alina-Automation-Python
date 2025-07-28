from pathlib import Path
import json
import logging
json_folder = Path(".")
log_file = json_folder / "json__vybyvanets.log"

logging.basicConfig(
    filename=log_file,
    level=logging.ERROR,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    encoding = 'utf-8',
)
json_files = list(json_folder.glob('*.json'))
for file in json_files:
    try:
        with open(file, "r", encoding="utf-8") as f:
            json.load(f)
        print (f"Файл {file.name} валідний")
    except json.JSONDecodeError as e:
        logging.error(f" {file.name} невалідний json: {e}")
        print(f"{file.name} невалідний(помилка записана в лог)")