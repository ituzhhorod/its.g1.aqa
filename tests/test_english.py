# coding=utf-8
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from helpers.assertions import *
from helpers.func import *
from helpers.locators import *


def test_click_english_it_button_on_homepage(driver):
    get_homepage(driver)
    # Перевірка кліку на кнопку Англійська для ІТ спеціалістів -> Детальніше
    button_click(driver, HOME_PAGE_BUTTON_DETAILS_ENGLISH)
    # Чекаємо на кнопку "Зареєструватись на іншій cторінці"
    wait_for_element(driver, ENLISH_PAGE_BUTTON_TEXT)
  # перевірити текст на новій сторінці
    assert_text_on_page(driver, "English for IT Specialists")


def test_click_automation_testing_button_on_homepage(driver):
    get_homepage(driver)
    # Перевірка кліку на кнопку Автоматизоване Тестування -> Детальніше
    button_click(driver, HOME_PAGE_BUTTON_DETAILS_AUTOMATION_TESTING)
    # Чекаємо на кнопку "Зареєструватись на іншій cторінці"
    wait_for_element(driver, AUTOMATION_TESTING_PAGE_BUTTON_REGISTER)
    # перевірити текст на новій сторінці
    assert_text_on_page(driver, "Automation QA")


def test_click_contact_button_on_homepage(driver):
    get_homepage(driver)
    # Перевірка кліку на кнопку Стань викладачем курсів -> Детальніше
    button_click(driver, HOME_PAGE_BUTTON_DETAILS_TEACHER_COURSES)
    # Чекаємо на кнопку "Зареєструватись на іншій cторінці"
    wait_for_element(driver, TEACHER_COURSES_PAGE_BUTTON_REGISTER)
    # перевірити текст на новій сторінці
    assert_text_on_page(driver, "December 12, 2017")
