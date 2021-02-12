# coding=utf-8
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers.assertions import *
from helpers.func import *
from helpers.locators import *


def test_title_homepage(driver):
   driver.get("https://its.uz.ua/")
   assert 'its.uz.ua' in driver.title


def test_click_base_qa_button_on_homepage(driver):
    get_homepage(driver)
    # Перевірка кліку на кнопку Базовий курс тестування (QA) -> Детальніше
    button_click(driver, HOME_PAGE_BUTTON_DETAILS_BASE_QA)
    # Чекаємо на кнопку "Зареєструватись на іншій чторінці"
    wait_for_element(driver, BASE_QA_PAGE_BUTTON_REGISTER)
    # перевірити текст на новій сторінці
    assert_text_on_page(driver, "Windows / Linux / MAC OS")

# https://its.uz.ua/services/base_qa
# Перевірити що список програми курсу - активни
# іконки - вимоги до студентів - присутні і активні


def test_get_title2(driver):
   driver.get("https://its.uz.ua/services/")
   assert 'its.uz.ua' in driver.title


def test_get_title3(driver):
   driver.get("https://its.uz.ua/services/base_qa")
   assert 'its.uz.ua' in driver.title

 def test_click_contact_button_on_homepage(driver):
   driver.get("https://its.uz.ua/")
   # Перевірка кліку на кнопку Станьте викладачем курсів -> Детальніше
   button = driver.find_element(By.CSS_SELECTOR, 'a[href="/contact"]')
   button.click()
   # Чекаємо на кнопку "Надіслати"
   WebDriverWait(driver, 10).until(
   EC.presence_of_element_located((By.CSS_SELECTOR,"#button")))
   # перевірити текст на новій сторінці
   contact_page = driver.find_element_by_tag_name("body")
   all_text_on_page = contact_page.text
   assert "December 12, 2017" in all_text_on_page
