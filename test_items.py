from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_we_should_see_on_button_languages(browser):
    browser.get(link)
    # time.sleep(30)
    assert WebDriverWait(browser, 5).until(
        ec.visibility_of_element_located((By.CSS_SELECTOR, "button.btn-add-to-basket")), "Кнопа не найдена!"
    )