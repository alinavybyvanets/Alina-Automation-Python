import logging
import xml.etree.ElementTree as ET

logger = logging.getLogger("xml_logger")
logger.setLevel(logging.INFO)
if not logger.handlers:
    ch = logging.StreamHandler()
    formatter = logging.Formatter("%(levelname)s - %(message)s")
    ch.setFormatter(formatter)
    logger.addHandler(ch)
XML_FILE ="groups.xml"

def find_incoming_by_group_number(group_number: str):
    tree = ET.parse(XML_FILE)
    root = tree.getroot()

    for group in root.findall("group"):
        number = group.find("number")
        if number is not None and number.text == group_number:
            incoming = group.find("timingExbytes/incoming")
            if incoming is not None:
                value = incoming.text
                logger.info(f"For group {group_number} incoming = {value}")
                return value
    logger.info(f"Group number {group_number} is not found.")
    return None
if __name__ == "__main__":
    find_incoming_by_group_number(group_number="0")