import pytest
from selenium import webdriver
import pytest


@pytest.fixture(scope="session")
def driver():
   options = webdriver.ChromeOptions()
   # options.headless = True
   options.add_argument("--window-size=1800,1600")
   d = webdriver.Chrome(options=options)
   d.implicitly_wait(1)
   return d


@pytest.fixture(scope="session")
def teardown():
    yield driver
    driver.close()

