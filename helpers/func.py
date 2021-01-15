from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_homepage(driver):
    driver.get("https://its.uz.ua/")


def button_click(driver, css_locator):
    button = driver.find_element(By.CSS_SELECTOR, css_locator)
    button.click()


def wait_for_element(driver, element_css_locator):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, element_css_locator)))

