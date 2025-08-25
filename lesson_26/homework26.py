from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL= "http://localhost:8000/dz.html"
SUCCESS_TEXT = "Верифікація пройшла успішно!"

FRAMES = [
    {"frame_id": "frame1", "input_id": "input1", "secret": "Frame1_Secret"},
    {"frame_id": "frame2", "input_id": "input2", "secret": "Frame2_Secret"},
]

def verify_frame(driver, frame_id: str, input_id: str, secret: str):
    wait = WebDriverWait(driver, 10)

    frame_el = wait.until(EC.presence_of_element_located((By.ID, frame_id)))
    driver.switch_to.frame(frame_el)

    input_el = wait.until(EC.visibility_of_element_located((By.ID, input_id)))
    input_el.clear()
    input_el.send_keys(secret)

    check_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Перевірити']")))
    check_btn.click()

    alert = wait.until(EC.alert_is_present())
    alert_text = alert.text.strip()
    assert alert_text == SUCCESS_TEXT, f'Очікував "{SUCCESS_TEXT}" але отримав "{alert_text}"'
    alert.accept()

    driver.switch_to.default_content()

def main():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        driver.get(URL)
        for f in FRAMES:
            verify_frame(driver, f["frame_id"], f["input_id"], f["secret"])
        print("Обидва фрейми успішно верифіковані.")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
