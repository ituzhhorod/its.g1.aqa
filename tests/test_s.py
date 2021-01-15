# coding=utf-8
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_get_title1(driver):
    driver.get("https://its.uz.ua/")
    element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR,
            "body > div.content > div:nth-child(1) > div > div:nth-child(1) > div > a")))
    element.click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR,
             "body > div.service-content > div.service-info1 > div > a")))
    assert 'its.uz.ua' in driver.title
